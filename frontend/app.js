
(() => {
    'use strict';

    const DISEASE_COLORS = {
        'Healthy': '#10B981',
        'Asthma': '#F59E0B',
        'COPD': '#EF4444',
        'Pneumonia': '#8B5CF6'
    };

    const DISEASE_ICONS = {
        'Healthy': '●',
        'Asthma': '●',
        'COPD': '●',
        'Pneumonia': '●'
    };

    const SEVERITY_COLORS = {
        'mild': '#10B981',
        'moderate': '#F59E0B',
        'severe': '#F97316',
        'critical': '#EF4444'
    };

    const TREATMENT_COLORS = {
        'medication': '#38bdf8',
        'therapy': '#10B981',
        'lifestyle': '#A78BFA',
        'surgical': '#F87171'
    };

    const CHART_COLORS = ['#10B981', '#F59E0B', '#EF4444', '#8B5CF6'];
    const MAX_FILE_SIZE = 10 * 1024 * 1024; 
    const ALLOWED_AUDIO_TYPES = [
        'audio/wav', 'audio/x-wav', 'audio/mpeg', 'audio/mp3',
        'audio/ogg', 'audio/flac', 'audio/x-flac', 'audio/webm',
        'audio/aac', 'audio/mp4'
    ];

    let selectedFile = null;
    let lastPrediction = null;
    let confidenceChart = null;
    let waveformChart = null;
    let audioContext = null;
    let scriptProcessor = null;
    let sourceNode = null;
    let audioSamples = [];
    let sampleRate = 22050;
    let recordingTimer = null;
    let recordingSeconds = 0;
    const MAX_RECORDING_SECONDS = 20;
    let playbackAudio = null;
    let playbackRAF = null;

    const $ = (sel) => document.querySelector(sel);
    const $$ = (sel) => document.querySelectorAll(sel);

    const dom = {
        navbar: $('#navbar'),
        navLinks: $('#nav-links'),
        navToggle: $('#nav-toggle'),
        uploadZone: $('#upload-zone'),
        fileInput: $('#file-input'),
        fileInfo: $('#file-info'),
        fileName: $('#file-name'),
        fileSize: $('#file-size'),
        fileRemove: $('#file-remove'),
        analyzeBtn: $('#analyze-btn'),
        btnText: null,       
        btnLoader: $('#btn-loader'),
        loadingOverlay: $('#loading-overlay'),
        resultsPanel: $('#results-panel'),
        predictionCard: $('#prediction-card'),
        predictionIcon: $('#prediction-icon'),
        predictionClass: $('#prediction-class'),
        predictionConfidence: $('#prediction-confidence'),
        predictionDescription: $('#prediction-description'),
        learnMoreBtn: $('#learn-more-btn'),
        confidenceCanvas: $('#confidence-chart'),
        waveformCanvas: $('#waveform-chart'),
        spectrogramImg: $('#spectrogram-img'),
        breakdownBars: $('#breakdown-bars'),
        diseaseModal: $('#disease-modal'),
        modalHeader: $('#modal-header'),
        modalIcon: $('#modal-icon'),
        modalDiseaseName: $('#modal-disease-name'),
        modalTagline: $('#modal-tagline'),
        modalClose: $('#modal-close'),
        modalTabs: $('#modal-tabs'),
        modalBody: $('#modal-body'),
        overviewStats: $('#overview-stats'),
        overviewText: $('#overview-text'),
        breathSoundsText: $('#breath-sounds-text'),
        symptomsGrid: $('#symptoms-grid'),
        causesGrid: $('#causes-grid'),
        stagesTimeline: $('#stages-timeline'),
        stagesSection: $('#stages-section'),
        treatmentsGrid: $('#treatments-grid'),
        diagnosisList: $('#diagnosis-list'),
        medicationsGrid: $('#medications-grid'),
        preventionGrid: $('#prevention-grid'),
        doctorAlertList: $('#doctor-alert-list'),
        referencesList: $('#references-list'),
        downloadReportBtn: $('#download-report-btn'),
        pdfReportContainer: $('#pdf-report-container'),
        
        micSection: $('#mic-section'),
        micBtn: $('#mic-btn'),
        micIcon: $('#mic-icon'),
        micPulse: $('#mic-pulse'),
        micLabel: $('#mic-label'),
        micTimer: $('#mic-timer'),
        timerText: $('#timer-text'),
        playbackSection: $('#playback-section'),
        playbackBtn: $('#playback-btn'),
        playbackIconPlay: $('#playback-icon-play'),
        playbackIconPause: $('#playback-icon-pause'),
        playbackTime: $('#playback-time'),
        playbackProgressTrack: $('#playback-progress-track'),
        playbackProgressFill: $('#playback-progress-fill')
    };

    dom.btnText = dom.analyzeBtn?.querySelector('.btn-text');

    function formatFileSize(bytes) {
        if (bytes === 0) return '0 B';
        if (bytes < 1024) return `${bytes} B`;
        if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
        return `${(bytes / (1024 * 1024)).toFixed(2)} MB`;
    }

    function escapeHTML(str) {
        if (!str) return '';
        const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
        return String(str).replace(/[&<>"']/g, (c) => map[c]);
    }

    function debounce(fn, delay = 100) {
        let timer;
        return (...args) => {
            clearTimeout(timer);
            timer = setTimeout(() => fn(...args), delay);
        };
    }

    function isAudioFile(file) {
        if (ALLOWED_AUDIO_TYPES.includes(file.type)) return true;
        const ext = file.name.split('.').pop().toLowerCase();
        return ['wav', 'mp3', 'ogg', 'flac', 'webm', 'aac', 'm4a'].includes(ext);
    }

    async function apiPost(url, body) {
        const res = await fetch(url, { method: 'POST', body });
        if (!res.ok) {
            const err = await res.json().catch(() => ({}));
            throw new Error(err.detail || `Server error (${res.status})`);
        }
        return res.json();
    }

    async function apiGet(url) {
        const res = await fetch(url);
        if (!res.ok) {
            const err = await res.json().catch(() => ({}));
            throw new Error(err.detail || `Server error (${res.status})`);
        }
        return res.json();
    }

    function initNavigation() {
        document.addEventListener('click', (e) => {
            const link = e.target.closest('a[href^="#"]');
            if (!link) return;
            const target = document.querySelector(link.getAttribute('href'));
            if (!target) return;
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth' });
            dom.navLinks?.classList.remove('open');
            dom.navToggle?.classList.remove('open');
        });

        dom.navToggle?.addEventListener('click', () => {
            dom.navLinks.classList.toggle('open');
            dom.navToggle.classList.toggle('open');
        });

        const onScroll = debounce(() => {
            if (!dom.navbar) return;
            if (window.scrollY > 50) {
                dom.navbar.classList.add('scrolled');
            } else {
                dom.navbar.classList.remove('scrolled');
            }
        }, 10);
        window.addEventListener('scroll', onScroll, { passive: true });

        const sections = $$('section[id]');
        if (sections.length) {
            const observer = new IntersectionObserver(
                (entries) => {
                    entries.forEach((entry) => {
                        if (entry.isIntersecting) {
                            const id = entry.target.id;
                            $$('.nav-link').forEach((link) => {
                                link.classList.toggle(
                                    'active',
                                    link.getAttribute('href') === `#${id}`
                                );
                            });
                        }
                    });
                },
                { rootMargin: '-20% 0px -75% 0px', threshold: 0 }
            );
            sections.forEach((s) => observer.observe(s));
        }
    }

    function initFileUpload() {
        dom.uploadZone?.addEventListener('click', () => dom.fileInput?.click());

        dom.uploadZone?.addEventListener('dragenter', (e) => {
            e.preventDefault();
            dom.uploadZone.classList.add('drag-over');
        });
        dom.uploadZone?.addEventListener('dragover', (e) => {
            e.preventDefault();
            dom.uploadZone.classList.add('drag-over');
        });
        dom.uploadZone?.addEventListener('dragleave', () => {
            dom.uploadZone.classList.remove('drag-over');
        });
        dom.uploadZone?.addEventListener('drop', (e) => {
            e.preventDefault();
            dom.uploadZone.classList.remove('drag-over');
            const file = e.dataTransfer?.files?.[0];
            if (file) handleFileSelection(file);
        });

        dom.fileInput?.addEventListener('change', () => {
            const file = dom.fileInput.files?.[0];
            if (file) handleFileSelection(file);
        });

        dom.fileRemove?.addEventListener('click', (e) => {
            e.stopPropagation();
            clearFile();
        });

        dom.analyzeBtn?.addEventListener('click', analyzeAudio);
    }

    function initMicrophone() {
        if (!dom.micBtn) return;

        dom.micBtn.addEventListener('click', async () => {
            if (audioContext && audioContext.state === 'running') {
                stopRecording();
            } else {
                await startRecording();
            }
        });
    }

    async function startRecording() {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ 
                audio: {
                    echoCancellation: true,
                    noiseSuppression: true
                } 
            });

            audioSamples = [];
            recordingSeconds = 0;

            audioContext = new (window.AudioContext || window.webkitAudioContext)({ sampleRate: 22050 });
            sampleRate = audioContext.sampleRate;

            sourceNode = audioContext.createMediaStreamSource(stream);
            
            scriptProcessor = audioContext.createScriptProcessor(4096, 1, 1);

            scriptProcessor.onaudioprocess = (e) => {
                const inputData = e.inputBuffer.getChannelData(0);
                audioSamples.push(new Float32Array(inputData));
            };

            sourceNode.connect(scriptProcessor);
            scriptProcessor.connect(audioContext.destination);

            dom.micBtn.classList.add('recording');
            dom.micPulse.classList.add('active');
            dom.micLabel.textContent = 'Recording... Tap to Stop';
            dom.micTimer.style.display = 'flex';
            updateTimerDisplay();

            recordingTimer = setInterval(() => {
                recordingSeconds++;
                updateTimerDisplay();
                if (recordingSeconds >= MAX_RECORDING_SECONDS) {
                    stopRecording();
                }
            }, 1000);

        } catch (err) {
            if (err.name === 'NotAllowedError') {
                showError('Microphone access denied. Please allow microphone access in your browser settings.');
            } else if (err.name === 'NotFoundError') {
                showError('No microphone found. Please connect a microphone and try again.');
            } else {
                showError(`Could not start recording: ${err.message}`);
            }
        }
    }

    function stopRecording() {
        clearInterval(recordingTimer);
        recordingTimer = null;

        if (scriptProcessor) {
            scriptProcessor.disconnect();
            scriptProcessor = null;
        }

        if (sourceNode) {
            if (sourceNode.mediaStream) {
                sourceNode.mediaStream.getTracks().forEach(t => t.stop());
            }
            sourceNode.disconnect();
            sourceNode = null;
        }

        if (audioContext) {
            audioContext.close();
            audioContext = null;
        }

        if (audioSamples.length === 0) {
            resetMicUI();
            showError('No audio recorded.');
            return;
        }

        const totalLength = audioSamples.reduce((acc, val) => acc + val.length, 0);
        const mergedBuffer = new Float32Array(totalLength);
        let offset = 0;
        for (const chunk of audioSamples) {
            mergedBuffer.set(chunk, offset);
            offset += chunk.length;
        }

        const wavBlob = encodeWAV(mergedBuffer, sampleRate);
        const file = new File([wavBlob], `recording_${Date.now()}.wav`, { type: 'audio/wav' });

        handleFileSelection(file);

        showPlayback(wavBlob);

        resetMicUI();
    }

    function encodeWAV(samples, sampleRate) {
        const buffer = new ArrayBuffer(44 + samples.length * 2);
        const view = new DataView(buffer);

        writeString(view, 0, 'RIFF');
        view.setUint32(4, 36 + samples.length * 2, true);
        writeString(view, 8, 'WAVE');
        writeString(view, 12, 'fmt ');
        view.setUint32(16, 16, true);
        view.setUint16(20, 1, true);
        view.setUint16(22, 1, true);
        view.setUint32(24, sampleRate, true);
        view.setUint32(28, sampleRate * 2, true);
        view.setUint16(32, 2, true);
        view.setUint16(34, 16, true);
        writeString(view, 36, 'data');
        view.setUint32(40, samples.length * 2, true);

        floatTo16BitPCM(view, 44, samples);

        return new Blob([view], { type: 'audio/wav' });
    }

    function floatTo16BitPCM(output, offset, input) {
        for (let i = 0; i < input.length; i++, offset += 2) {
            let s = Math.max(-1, Math.min(1, input[i]));
            output.setInt16(offset, s < 0 ? s * 0x8000 : s * 0x7FFF, true);
        }
    }

    function writeString(view, offset, string) {
        for (let i = 0; i < string.length; i++) {
            view.setUint8(offset + i, string.charCodeAt(i));
        }
    }

    function resetMicUI() {
        dom.micBtn.classList.remove('recording');
        dom.micPulse.classList.remove('active');
        dom.micLabel.textContent = 'Tap to Record';
        dom.micTimer.style.display = 'none';
        recordingSeconds = 0;
    }

    function updateTimerDisplay() {
        const mins = String(Math.floor(recordingSeconds / 60)).padStart(2, '0');
        const secs = String(recordingSeconds % 60).padStart(2, '0');
        if (dom.timerText) dom.timerText.textContent = `${mins}:${secs}`;
    }

    function handleFileSelection(file) {
        if (!isAudioFile(file)) {
            showError('Please upload an audio file (.wav, .mp3, .ogg, .flac).');
            return;
        }
        if (file.size > MAX_FILE_SIZE) {
            showError(`File too large. Maximum size is ${formatFileSize(MAX_FILE_SIZE)}.`);
            return;
        }

        selectedFile = file;
        dom.fileName.textContent = file.name;
        dom.fileSize.textContent = formatFileSize(file.size);
        dom.fileInfo.style.display = 'flex';
        dom.analyzeBtn.disabled = false;
    }

    function clearFile() {
        selectedFile = null;
        if (dom.fileInput) dom.fileInput.value = '';
        dom.fileInfo.style.display = 'none';
        dom.fileName.textContent = '';
        dom.fileSize.textContent = '';
        dom.analyzeBtn.disabled = true;
        hidePlayback();
    }

    async function analyzeAudio() {
        if (!selectedFile) return;

        dom.loadingOverlay.style.display = 'flex';
        dom.analyzeBtn.disabled = true;
        if (dom.btnText) dom.btnText.textContent = 'Analyzing...';
        dom.btnLoader.style.display = 'inline-flex';

        try {
            const formData = new FormData();
            formData.append('file', selectedFile);
            let result = await apiPost('/api/predict', formData);
            
            lastPrediction = result;
            renderResults(result);
        } catch (err) {
            showError(err.message || 'Analysis failed. Please try again.');
        } finally {
            dom.loadingOverlay.style.display = 'none';
            dom.analyzeBtn.disabled = false;
            if (dom.btnText) dom.btnText.textContent = 'Analyze Breath Sound';
            dom.btnLoader.style.display = 'none';
        }
    }

    function renderResults(result) {
        const { confidences, top_class, top_confidence, description, spectrogram, waveform } = result;
        const color = DISEASE_COLORS[top_class] || '#8B5CF6';
        const icon = DISEASE_ICONS[top_class] || '❓';

        dom.resultsPanel.style.display = 'flex';
        const analyzerLayout = document.querySelector('.analyzer-layout');
        if (analyzerLayout) analyzerLayout.classList.add('has-results');

        dom.predictionCard.style.borderLeftColor = color;
        dom.predictionIcon.textContent = icon;
        dom.predictionClass.textContent = top_class;
        dom.predictionConfidence.textContent = `${top_confidence.toFixed(1)}%`;
        dom.predictionConfidence.style.color = color;
        dom.predictionDescription.textContent = description;

        renderDonutChart(confidences, top_class, top_confidence);
        renderWaveformChart(waveform);

        if (spectrogram) {
            dom.spectrogramImg.src = `data:image/png;base64,${spectrogram}`;
            dom.spectrogramImg.alt = 'Mel spectrogram of uploaded breath sound';
        }

        renderBreakdownBars(confidences);

        setTimeout(() => {
            dom.resultsPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 200);
    }

    function renderDonutChart(confidences, topClass, topConfidence) {
        if (confidenceChart) {
            confidenceChart.destroy();
            confidenceChart = null;
        }

        const labels = Object.keys(confidences);
        const data = Object.values(confidences);
        const colors = labels.map((l) => DISEASE_COLORS[l] || '#94a3b8');

        const centerTextPlugin = {
            id: 'centerText',
            afterDraw(chart) {
                const { ctx, chartArea: { top, bottom, left, right } } = chart;
                const centerX = (left + right) / 2;
                const centerY = (top + bottom) / 2;

                ctx.save();
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';

                ctx.font = 'bold 28px Inter, sans-serif';
                ctx.fillStyle = DISEASE_COLORS[topClass] || '#e2e8f0';
                ctx.fillText(`${topConfidence.toFixed(1)}%`, centerX, centerY - 8);

                ctx.font = '12px Inter, sans-serif';
                ctx.fillStyle = '#94a3b8';
                ctx.fillText(topClass, centerX, centerY + 16);

                ctx.restore();
            }
        };

        confidenceChart = new Chart(dom.confidenceCanvas, {
            type: 'doughnut',
            data: {
                labels,
                datasets: [{
                    data,
                    backgroundColor: colors,
                    borderColor: 'rgba(15, 23, 42, 0.8)',
                    borderWidth: 2,
                    hoverOffset: 8
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                cutout: '70%',
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        backgroundColor: 'rgba(15, 23, 42, 0.9)',
                        titleColor: '#e2e8f0',
                        bodyColor: '#cbd5e1',
                        borderColor: 'rgba(148, 163, 184, 0.2)',
                        borderWidth: 1,
                        padding: 12,
                        cornerRadius: 8,
                        callbacks: {
                            label: (ctx) => ` ${ctx.label}: ${ctx.parsed.toFixed(1)}%`
                        }
                    }
                },
                animation: {
                    animateRotate: true,
                    duration: 1000,
                    easing: 'easeOutQuart'
                }
            },
            plugins: [centerTextPlugin]
        });
    }

    function renderWaveformChart(waveformData) {
        if (waveformChart) {
            waveformChart.destroy();
            waveformChart = null;
        }

        if (!waveformData || !waveformData.length) return;

        const ctx = dom.waveformCanvas.getContext('2d');
        const gradient = ctx.createLinearGradient(0, 0, dom.waveformCanvas.width, 0);
        gradient.addColorStop(0, '#38bdf8');
        gradient.addColorStop(1, '#818cf8');

        waveformChart = new Chart(dom.waveformCanvas, {
            type: 'bar',
            data: {
                labels: waveformData.map((_, i) => i),
                datasets: [{
                    data: waveformData,
                    backgroundColor: gradient,
                    borderRadius: 2,
                    barPercentage: 0.9,
                    categoryPercentage: 1.0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false },
                    tooltip: { enabled: false }
                },
                scales: {
                    x: {
                        display: false,
                        grid: { display: false }
                    },
                    y: {
                        display: false,
                        grid: { display: false },
                        beginAtZero: true,
                        max: 1
                    }
                },
                animation: {
                    duration: 800,
                    easing: 'easeOutQuart'
                }
            }
        });
    }

    function renderBreakdownBars(confidences) {
        dom.breakdownBars.innerHTML = '';

        const sorted = Object.entries(confidences).sort((a, b) => b[1] - a[1]);

        sorted.forEach(([name, value], idx) => {
            const color = DISEASE_COLORS[name] || '#94a3b8';
            const icon = DISEASE_ICONS[name] || '❓';

            const item = document.createElement('div');
            item.className = 'breakdown-bar-item';
            item.innerHTML = `
                <div class="bar-header">
                    <span class="bar-label"><span style="color:${color}">${icon}</span> ${escapeHTML(name)}</span>
                    <span class="bar-value">${value.toFixed(1)}%</span>
                </div>
                <div class="bar-track">
                    <div class="bar-fill" style="width: 0%; background: ${color};"></div>
                </div>
            `;
            dom.breakdownBars.appendChild(item);

            const fill = item.querySelector('.bar-fill');
            setTimeout(() => {
                fill.style.transition = 'width 0.6s cubic-bezier(0.22, 1, 0.36, 1)';
                fill.style.width = `${value}%`;
            }, 100 + idx * 120);
        });
    }

    function initDiseaseCards() {
        const grid = document.querySelector('.disease-grid');
        if (grid) {
            grid.addEventListener('click', (e) => {
                const card = e.target.closest('.disease-card');
                if (card) openDiseaseModal(card.dataset.disease);
            });
            grid.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    const card = e.target.closest('.disease-card');
                    if (card) {
                        e.preventDefault();
                        openDiseaseModal(card.dataset.disease);
                    }
                }
            });
        }
    }

    async function openDiseaseModal(diseaseId) {
        if (!diseaseId) return;

        try {
            dom.diseaseModal.style.display = 'flex';
            document.body.style.overflow = 'hidden';

            const disease = await apiGet(`/api/diseases/${diseaseId}`);
            populateModal(disease);
        } catch (err) {
            closeModal();
            showError(`Could not load disease details: ${err.message}`);
        }
    }

    function populateModal(d) {
        const color = d.color || DISEASE_COLORS[d.name] || '#8B5CF6';

        dom.modalIcon.textContent = d.icon || '';
        dom.modalDiseaseName.textContent = d.name;
        dom.modalTagline.textContent = d.tagline || '';
        dom.modalHeader.style.background = `linear-gradient(135deg, ${color}22, ${color}08)`;
        dom.modalHeader.style.borderBottomColor = `${color}33`;

        $$('.tab-btn').forEach((b) => b.classList.remove('active'));
        $$('.tab-content').forEach((c) => c.classList.remove('active'));
        const firstTab = $('.tab-btn[data-tab="overview"]');
        if (firstTab) firstTab.classList.add('active');
        const overviewTab = $('#tab-overview');
        if (overviewTab) overviewTab.classList.add('active');

        const stats = d.statistics || {};
        const statItems = [
            { label: 'Prevalence', value: stats.prevalence, icon: '' },
            { label: 'Annual Deaths', value: stats.annual_deaths, icon: '' },
            { label: 'Age Group', value: stats.age_group, icon: '' },
            { label: 'Trend', value: stats.trend, icon: '' }
        ];
        dom.overviewStats.innerHTML = statItems
            .map((s) => `
                <div class="stat-card">
                    <span class="stat-card-icon">${s.icon}</span>
                    <span class="stat-card-value">${escapeHTML(s.value || 'N/A')}</span>
                    <span class="stat-card-label">${escapeHTML(s.label)}</span>
                </div>
            `).join('');

        const overviewParagraphs = (d.overview || '').split('\n\n').filter(Boolean);
        dom.overviewText.innerHTML = overviewParagraphs
            .map((p) => `<p>${escapeHTML(p)}</p>`).join('');

        dom.breathSoundsText.textContent = d.breath_sounds || 'No information available.';

        const symptoms = d.symptoms || [];
        dom.symptomsGrid.innerHTML = symptoms.map((s) => `
            <div class="symptom-card">
                <span class="symptom-icon">${s.icon || '•'}</span>
                <h5 class="symptom-name">${escapeHTML(s.name)}</h5>
                <p class="symptom-desc">${escapeHTML(s.description)}</p>
            </div>
        `).join('');

        const causes = d.causes_risk_factors || [];
        dom.causesGrid.innerHTML = causes.map((c) => `
            <div class="cause-card">
                <span class="cause-icon">${c.icon || '•'}</span>
                <h5 class="cause-name">${escapeHTML(c.name)}</h5>
                <p class="cause-desc">${escapeHTML(c.description)}</p>
            </div>
        `).join('');

        const stages = d.stages || [];
        if (stages.length) {
            dom.stagesSection.style.display = 'block';
            dom.stagesTimeline.innerHTML = stages.map((s) => {
                const sevColor = SEVERITY_COLORS[s.severity] || '#94a3b8';
                return `
                    <div class="stage-item" style="--stage-color: ${sevColor};">
                        <div class="stage-marker" style="background: ${sevColor};"></div>
                        <div class="stage-content">
                            <div class="stage-header">
                                <h5 class="stage-name">${escapeHTML(s.name)}</h5>
                                <span class="severity-badge" style="background: ${sevColor}20; color: ${sevColor};">${escapeHTML(s.severity)}</span>
                            </div>
                            <p class="stage-desc">${escapeHTML(s.description)}</p>
                        </div>
                    </div>
                `;
            }).join('');
        } else {
            dom.stagesSection.style.display = 'none';
        }

        const treatments = d.treatments || [];
        dom.treatmentsGrid.innerHTML = treatments.map((t) => {
            const tColor = TREATMENT_COLORS[t.type] || '#94a3b8';
            return `
                <div class="treatment-card">
                    <div class="treatment-header">
                        <h5 class="treatment-name">${escapeHTML(t.name)}</h5>
                        <span class="treatment-type-badge" style="background: ${tColor}20; color: ${tColor};">${escapeHTML(t.type)}</span>
                    </div>
                    <p class="treatment-desc">${escapeHTML(t.description)}</p>
                </div>
            `;
        }).join('');

        const diagnosis = d.diagnosis || [];
        dom.diagnosisList.innerHTML = diagnosis.map((dx) => `
            <div class="diagnosis-item">
                <h5 class="diagnosis-method">${escapeHTML(dx.method)}</h5>
                <p class="diagnosis-desc">${escapeHTML(dx.description)}</p>
            </div>
        `).join('');

        const meds = d.medications || [];
        dom.medicationsGrid.innerHTML = meds.map((m) => `
            <div class="medication-card">
                <div class="med-header">
                    <h5 class="med-name">${escapeHTML(m.name)}</h5>
                    <span class="med-type-badge">${escapeHTML(m.type)}</span>
                </div>
                ${m.generic_name ? `<p class="med-generic"><em>${escapeHTML(m.generic_name)}</em></p>` : ''}
                <p class="med-description">${escapeHTML(m.description)}</p>
                ${m.usage ? `<div class="med-usage-box"><strong>Usage:</strong> ${escapeHTML(m.usage)}</div>` : ''}
                ${m.side_effects?.length ? `
                    <div class="med-side-effects">
                        <strong>Side Effects:</strong>
                        <div class="side-effect-chips">
                            ${m.side_effects.map((se) => `<span class="chip">${escapeHTML(se)}</span>`).join('')}
                        </div>
                    </div>
                ` : ''}
            </div>
        `).join('');

        const prevention = d.prevention || [];
        dom.preventionGrid.innerHTML = prevention.map((p) => `
            <div class="prevention-card">
                <span class="prevention-icon">${p.icon || '💡'}</span>
                <h5 class="prevention-tip">${escapeHTML(p.tip)}</h5>
                <p class="prevention-desc">${escapeHTML(p.description)}</p>
            </div>
        `).join('');

        const doctorList = d.when_to_see_doctor || [];
        dom.doctorAlertList.innerHTML = doctorList
            .map((item) => `<li>${escapeHTML(item)}</li>`).join('');

        const refs = d.references || [];
        dom.referencesList.innerHTML = refs.map((r) => `
            <a class="reference-link" href="${escapeHTML(r.url)}" target="_blank" rel="noopener noreferrer">
                <span class="ref-title">${escapeHTML(r.title)}</span>
                <span class="ref-source">${escapeHTML(r.source)}</span>
            </a>
        `).join('');
    }

    function initModalTabs() {
        dom.modalTabs?.addEventListener('click', (e) => {
            const btn = e.target.closest('.tab-btn');
            if (!btn) return;

            const tab = btn.dataset.tab;
            $$('.tab-btn').forEach((b) => b.classList.remove('active'));
            $$('.tab-content').forEach((c) => c.classList.remove('active'));

            btn.classList.add('active');
            const target = $(`#tab-${tab}`);
            if (target) target.classList.add('active');
        });
    }

    function initModalClose() {
        dom.modalClose?.addEventListener('click', closeModal);

        dom.diseaseModal?.addEventListener('click', (e) => {
            if (e.target === dom.diseaseModal) closeModal();
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && dom.diseaseModal?.style.display !== 'none') {
                closeModal();
            }
        });
    }

    function closeModal() {
        dom.diseaseModal.style.display = 'none';
        document.body.style.overflow = '';
    }

    function initLearnMore() {
        dom.learnMoreBtn?.addEventListener('click', () => {
            if (!lastPrediction) return;
            const topClass = lastPrediction.top_class;
            const diseaseId = topClass.toLowerCase();
            openDiseaseModal(diseaseId);
        });
    }

    function initScrollAnimations() {
        const elements = $$('.animate-on-scroll');
        if (!elements.length) return;

        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        const parent = entry.target.parentElement;
                        const siblings = parent ? [...parent.querySelectorAll('.animate-on-scroll')] : [];
                        const idx = siblings.indexOf(entry.target);
                        const delay = idx >= 0 ? idx * 100 : 0;

                        setTimeout(() => {
                            entry.target.classList.add('visible');
                        }, delay);

                        observer.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.1 }
        );

        elements.forEach((el) => observer.observe(el));
    }

    function initDownloadReport() {
        if (!dom.downloadReportBtn) return;
        dom.downloadReportBtn.addEventListener('click', generatePDFReport);
    }

    async function generatePDFReport() {
        if (!lastPrediction) return;

        const btn = dom.downloadReportBtn;
        const originalText = btn.innerHTML;
        btn.disabled = true;
        btn.innerHTML = '<span class="spinner" style="width:14px; height:14px; border-width:2px; display:inline-block; margin-right:6px; border-top-color:transparent;"></span> Generating...';

        try {
            const sanitizeText = (str) => {
                if (!str) return '';
                return str
                    .replace(/≥/g, '>=')
                    .replace(/≤/g, '<=')
                    .replace(/•/g, '-')
                    .replace(/—/g, '-')
                    .replace(/–/g, '-')
                    .replace(/™/g, '')
                    .replace(/®/g, '(R)')
                    .replace(/[“”]/g, '"')
                    .replace(/[‘’]/g, "'");
            };

            const topClass = sanitizeText(lastPrediction.top_class);
            const diseaseId = topClass.toLowerCase();
            
            const rawDisease = await apiGet(`/api/diseases/${diseaseId}`);
            
            let spectrogramData = null;
            if (dom.spectrogramImg && dom.spectrogramImg.src && dom.spectrogramImg.src.startsWith('data:')) {
                spectrogramData = dom.spectrogramImg.src;
            } else if (lastPrediction.spectrogram) {
                spectrogramData = `data:image/png;base64,${lastPrediction.spectrogram}`;
            }

            let waveformData = null;
            if (waveformChart) {
                try {
                    waveformData = waveformChart.toBase64Image();
                } catch (e) {
                    console.error(e);
                }
            }
            
            const disease = {
                name: sanitizeText(rawDisease.name),
                symptoms: (rawDisease.symptoms || []).map(s => ({
                    name: sanitizeText(s.name),
                    description: sanitizeText(s.description)
                })),
                causes_risk_factors: (rawDisease.causes_risk_factors || []).map(c => ({
                    name: sanitizeText(c.name),
                    description: sanitizeText(c.description)
                })),
                treatments: (rawDisease.treatments || []).map(t => ({
                    name: sanitizeText(t.name),
                    description: sanitizeText(t.description)
                })),
                prevention: (rawDisease.prevention || []).map(p => ({
                    tip: sanitizeText(p.tip),
                    description: sanitizeText(p.description)
                })),
                medications: (rawDisease.medications || []).map(m => ({
                    name: sanitizeText(m.name),
                    generic_name: sanitizeText(m.generic_name),
                    description: sanitizeText(m.description)
                }))
            };
            
            const lastPredDesc = sanitizeText(lastPrediction.description);
            
            const jsPDFObj = (window.jspdf && window.jspdf.jsPDF) || window.jsPDF;
            if (!jsPDFObj) {
                throw new Error("jsPDF library not loaded");
            }
            
            const doc = new jsPDFObj({
                orientation: 'portrait',
                unit: 'mm',
                format: 'letter'
            });
            
            const dateStr = new Date().toLocaleString();
            
            const marginX = 15;
            const contentWidth = 185.9;
            const colWidth = 88;
            const colGap = 9.9;
            const col2X = marginX + colWidth + colGap;
            const rightEdge = 200.9;
            
            let y = 15;
            
            doc.setFont('helvetica', 'bold');
            doc.setFontSize(12);
            doc.setTextColor(17, 24, 39);
            doc.text('R.V. COLLEGE OF ENGINEERING', marginX, y + 4);
            
            doc.setFont('helvetica', 'normal');
            doc.setFontSize(8);
            doc.setTextColor(107, 114, 128);
            doc.text('Autonomous Institution affiliated to VTU, Bengaluru', marginX, y + 8);
            doc.text('Rashtreeya Sikshana Samithi Trust', marginX, y + 12);
            
            doc.setFont('helvetica', 'bold');
            doc.setFontSize(13.5);
            doc.setTextColor(20, 184, 166);
            doc.text('BreathAnalysis Diagnostic Report', rightEdge, y + 4, { align: 'right' });
            
            doc.setFont('helvetica', 'normal');
            doc.setFontSize(8);
            doc.setTextColor(107, 114, 128);
            doc.text(`Date: ${dateStr}`, rightEdge, y + 8.5, { align: 'right' });
            doc.text('DTL Project 2026', rightEdge, y + 12.5, { align: 'right' });
            
            y += 16;
            doc.setDrawColor(20, 184, 166);
            doc.setLineWidth(0.5);
            doc.line(marginX, y, rightEdge, y);
            
            y += 4;
            doc.setFillColor(243, 244, 246);
            doc.rect(marginX, y, contentWidth, 16, 'F');
            
            doc.setFont('helvetica', 'bold');
            doc.setFontSize(9);
            doc.setTextColor(75, 85, 99);
            
            doc.text('Primary Category:', marginX + 4, y + 5.5);
            doc.setFont('helvetica', 'bold');
            doc.setTextColor(17, 24, 39);
            doc.text(`${topClass}`, marginX + 35, y + 5.5);
            
            doc.setFont('helvetica', 'bold');
            doc.setTextColor(75, 85, 99);
            doc.text('Recording Length:', marginX + 105, y + 5.5);
            doc.setFont('helvetica', 'normal');
            doc.setTextColor(17, 24, 39);
            doc.text(`${lastPrediction.duration} seconds`, marginX + 138, y + 5.5);
            
            doc.setFont('helvetica', 'bold');
            doc.setTextColor(75, 85, 99);
            doc.text('Confidence Score:', marginX + 4, y + 11.5);
            doc.setFont('helvetica', 'bold');
            doc.setTextColor(20, 184, 166);
            doc.text(`${lastPrediction.top_confidence.toFixed(1)}%`, marginX + 35, y + 11.5);
            
            doc.setFont('helvetica', 'bold');
            doc.setTextColor(75, 85, 99);
            doc.text('Pipeline Framework:', marginX + 105, y + 11.5);
            doc.setFont('helvetica', 'normal');
            doc.setTextColor(17, 24, 39);
            doc.text('ResNet-18 + ICBHI Dataset', marginX + 138, y + 11.5);
            
            y += 21;
            
            doc.setFillColor(240, 253, 250);
            doc.setDrawColor(204, 251, 241);
            doc.setLineWidth(0.3);
            
            const descLines = doc.splitTextToSize(lastPredDesc, contentWidth - 8);
            const boxHeight = (descLines.length * 4.2) + 10;
            
            doc.rect(marginX, y, contentWidth, boxHeight, 'FD');
            
            doc.setDrawColor(20, 184, 166);
            doc.setLineWidth(1.2);
            doc.line(marginX, y, marginX, y + boxHeight);
            
            doc.setFont('helvetica', 'bold');
            doc.setFontSize(9.5);
            doc.setTextColor(15, 118, 110);
            doc.text('Classification Detail:', marginX + 4, y + 5);
            
            doc.setFont('helvetica', 'normal');
            doc.setFontSize(9);
            let lineY = y + 9.5;
            descLines.forEach((lineText) => {
                doc.text(lineText, marginX + 4, lineY);
                lineY += 4.2;
            });
            
            y += boxHeight + 8;
            
            doc.setFont('helvetica', 'bold');
            doc.setFontSize(10);
            doc.setTextColor(17, 24, 39);
            doc.text('Acoustic Visualizations', marginX, y);
            
            doc.setDrawColor(20, 184, 166);
            doc.setLineWidth(0.4);
            doc.line(marginX, y + 1.5, rightEdge, y + 1.5);
            y += 5.5;
            
            const imgBlockHeight = 24;
            
            doc.setFillColor(249, 250, 251);
            doc.setDrawColor(229, 231, 235);
            doc.setLineWidth(0.3);
            doc.rect(marginX, y, colWidth, imgBlockHeight, 'F');
            
            doc.setFont('helvetica', 'bold');
            doc.setFontSize(7.5);
            doc.setTextColor(107, 114, 128);
            doc.text('Mel Spectrogram', marginX + 3, y + 4);
            
            if (spectrogramData) {
                try {
                    doc.setFillColor(10, 15, 26);
                    doc.rect(marginX + 3, y + 6, colWidth - 6, imgBlockHeight - 9, 'F');
                    doc.addImage(spectrogramData, 'PNG', marginX + 3, y + 6, colWidth - 6, imgBlockHeight - 9);
                } catch (e) {
                    console.error(e);
                    doc.setFont('helvetica', 'italic');
                    doc.text('Image load error', marginX + 6, y + 12);
                }
            } else {
                doc.setFont('helvetica', 'italic');
                doc.text('No spectrogram available', marginX + 6, y + 12);
            }
            
            doc.setFillColor(249, 250, 251);
            doc.rect(col2X, y, colWidth, imgBlockHeight, 'F');
            
            doc.setFont('helvetica', 'bold');
            doc.setFontSize(7.5);
            doc.setTextColor(107, 114, 128);
            doc.text('Audio Waveform (RMS)', col2X + 3, y + 4);
            
            if (waveformData) {
                try {
                    doc.setFillColor(10, 15, 26);
                    doc.rect(col2X + 3, y + 6, colWidth - 6, imgBlockHeight - 9, 'F');
                    doc.addImage(waveformData, 'PNG', col2X + 3, y + 6, colWidth - 6, imgBlockHeight - 9);
                } catch (e) {
                    console.error(e);
                    doc.setFont('helvetica', 'italic');
                    doc.text('Image load error', col2X + 6, y + 12);
                }
            } else {
                doc.setFont('helvetica', 'italic');
                doc.text('No waveform available', col2X + 6, y + 12);
            }
            
            y += imgBlockHeight + 7;
            
            doc.setFont('helvetica', 'bold');
            doc.setFontSize(11);
            doc.setTextColor(17, 24, 39);
            doc.text(`Clinical Reference: ${disease.name}`, marginX, y);
            
            doc.setDrawColor(20, 184, 166);
            doc.setLineWidth(0.4);
            doc.line(marginX, y + 2, rightEdge, y + 2);
            
            y += 7;
            
            const colStartY = y;
            let leftY = colStartY;
            let rightY = colStartY;
            
            doc.setFont('helvetica', 'bold');
            doc.setFontSize(9.5);
            doc.setTextColor(17, 24, 39);
            doc.text('Recognized Symptoms', marginX, leftY);
            
            doc.setDrawColor(20, 184, 166);
            doc.setLineWidth(0.3);
            doc.line(marginX, leftY + 1.5, marginX + colWidth, leftY + 1.5);
            leftY += 5.5;
            
            const symptoms = disease.symptoms.slice(0, 3);
            if (symptoms.length === 0) {
                doc.setFont('helvetica', 'italic');
                doc.setFontSize(8.5);
                doc.setTextColor(107, 114, 128);
                doc.text('No specific symptoms cataloged.', marginX, leftY);
                leftY += 5;
            } else {
                symptoms.forEach(s => {
                    doc.setFont('helvetica', 'bold');
                    doc.setFontSize(8.5);
                    doc.setTextColor(55, 65, 81);
                    doc.text(`• ${s.name}:`, marginX, leftY);
                    
                    const sDesc = s.description.split('.')[0] + '.';
                    doc.setFont('helvetica', 'normal');
                    doc.setFontSize(8);
                    doc.setTextColor(75, 85, 99);
                    const wrappedLines = doc.splitTextToSize(sDesc, colWidth - 4);
                    wrappedLines.forEach(line => {
                        leftY += 3.8;
                        doc.text(line, marginX + 3.5, leftY);
                    });
                    leftY += 6;
                });
            }
            
            leftY += 2;
            doc.setFont('helvetica', 'bold');
            doc.setFontSize(9.5);
            doc.setTextColor(17, 24, 39);
            doc.text('Treatments & Interventions', marginX, leftY);
            
            doc.setDrawColor(20, 184, 166);
            doc.setLineWidth(0.3);
            doc.line(marginX, leftY + 1.5, marginX + colWidth, leftY + 1.5);
            leftY += 5.5;
            
            const treatments = disease.treatments.slice(0, 3);
            if (treatments.length === 0) {
                doc.setFont('helvetica', 'italic');
                doc.setFontSize(8.5);
                doc.setTextColor(107, 114, 128);
                doc.text('No specific treatments cataloged.', marginX, leftY);
                leftY += 5;
            } else {
                treatments.forEach(t => {
                    doc.setFont('helvetica', 'bold');
                    doc.setFontSize(8.5);
                    doc.setTextColor(55, 65, 81);
                    doc.text(`• ${t.name}:`, marginX, leftY);
                    
                    const tDesc = t.description.split('.')[0] + '.';
                    doc.setFont('helvetica', 'normal');
                    doc.setFontSize(8);
                    doc.setTextColor(75, 85, 99);
                    const wrappedLines = doc.splitTextToSize(tDesc, colWidth - 4);
                    wrappedLines.forEach(line => {
                        leftY += 3.8;
                        doc.text(line, marginX + 3.5, leftY);
                    });
                    leftY += 6;
                });
            }
            
            doc.setFont('helvetica', 'bold');
            doc.setFontSize(9.5);
            doc.setTextColor(17, 24, 39);
            doc.text('Triggers & Causes', col2X, rightY);
            
            doc.setDrawColor(20, 184, 166);
            doc.setLineWidth(0.3);
            doc.line(col2X, rightY + 1.5, col2X + colWidth, rightY + 1.5);
            rightY += 5.5;
            
            const causes = disease.causes_risk_factors.slice(0, 3);
            if (causes.length === 0) {
                doc.setFont('helvetica', 'italic');
                doc.setFontSize(8.5);
                doc.setTextColor(107, 114, 128);
                doc.text('No specific risk factors cataloged.', col2X, rightY);
                rightY += 5;
            } else {
                causes.forEach(c => {
                    doc.setFont('helvetica', 'bold');
                    doc.setFontSize(8.5);
                    doc.setTextColor(55, 65, 81);
                    doc.text(`• ${c.name}:`, col2X, rightY);
                    
                    const cDesc = c.description.split('.')[0] + '.';
                    doc.setFont('helvetica', 'normal');
                    doc.setFontSize(8);
                    doc.setTextColor(75, 85, 99);
                    const wrappedLines = doc.splitTextToSize(cDesc, colWidth - 4);
                    wrappedLines.forEach(line => {
                        rightY += 3.8;
                        doc.text(line, col2X + 3.5, rightY);
                    });
                    rightY += 6;
                });
            }
            
            rightY += 2;
            doc.setFont('helvetica', 'bold');
            doc.setFontSize(9.5);
            doc.setTextColor(17, 24, 39);
            doc.text('Preventative Measures', col2X, rightY);
            
            doc.setDrawColor(20, 184, 166);
            doc.setLineWidth(0.3);
            doc.line(col2X, rightY + 1.5, col2X + colWidth, rightY + 1.5);
            rightY += 5.5;
            
            const prevention = disease.prevention.slice(0, 3);
            if (prevention.length === 0) {
                doc.setFont('helvetica', 'italic');
                doc.setFontSize(8.5);
                doc.setTextColor(107, 114, 128);
                doc.text('No specific prevention tips cataloged.', col2X, rightY);
                rightY += 5;
            } else {
                prevention.forEach(p => {
                    doc.setFont('helvetica', 'bold');
                    doc.setFontSize(8.5);
                    doc.setTextColor(55, 65, 81);
                    doc.text(`• ${p.tip}:`, col2X, rightY);
                    
                    const pDesc = p.description.split('.')[0] + '.';
                    doc.setFont('helvetica', 'normal');
                    doc.setFontSize(8);
                    doc.setTextColor(75, 85, 99);
                    const wrappedLines = doc.splitTextToSize(pDesc, colWidth - 4);
                    wrappedLines.forEach(line => {
                        rightY += 3.8;
                        doc.text(line, col2X + 3.5, rightY);
                    });
                    rightY += 6;
                });
            }
            
            y = Math.max(leftY, rightY) + 5;
            
            const medications = disease.medications.slice(0, 2);
            if (medications.length > 0) {
                doc.setFont('helvetica', 'bold');
                doc.setFontSize(9.5);
                doc.setTextColor(17, 24, 39);
                doc.text('Recommended / Standard Medications', marginX, y);
                
                doc.setDrawColor(20, 184, 166);
                doc.setLineWidth(0.3);
                doc.line(marginX, y + 1.5, rightEdge, y + 1.5);
                y += 5.5;
                
                medications.forEach((med, index) => {
                    const medX = index === 0 ? marginX : col2X;
                    
                    doc.setFillColor(249, 250, 251);
                    doc.rect(medX, y, colWidth, 18, 'F');
                    
                    doc.setDrawColor(20, 184, 166);
                    doc.setLineWidth(0.8);
                    doc.line(medX, y, medX, y + 18);
                    
                    doc.setFont('helvetica', 'bold');
                    doc.setFontSize(8.5);
                    doc.setTextColor(17, 24, 39);
                    
                    const medHeader = med.name + (med.generic_name ? ` (${med.generic_name})` : '');
                    doc.text(medHeader, medX + 3, y + 4.5);
                    
                    doc.setFont('helvetica', 'normal');
                    doc.setFontSize(7.5);
                    doc.setTextColor(75, 85, 99);
                    
                    const mDesc = med.description.split('.')[0] + '.';
                    const wrappedMDesc = doc.splitTextToSize(mDesc, colWidth - 6);
                    let medY = y + 8.5;
                    wrappedMDesc.forEach(line => {
                        doc.text(line, medX + 3, medY);
                        medY += 3.4;
                    });
                });
                
                y += 24;
            }
            
            const footerY = 262;
            doc.setDrawColor(229, 231, 235);
            doc.setLineWidth(0.3);
            doc.line(marginX, footerY, rightEdge, footerY);
            
            doc.setFont('helvetica', 'normal');
            doc.setFontSize(7.5);
            doc.setTextColor(156, 163, 175);
            doc.text('This diagnostic report is dynamically synthesized by BreathAnalysis using convolutional neural network audio predictions.', 107.9, footerY + 4, { align: 'center' });
            doc.text('Educational College Project by Aryan K Ail • Ayush Khare • Abhinav Racha • Aditya Singh', 107.9, footerY + 8, { align: 'center' });
            
            doc.setFont('helvetica', 'bold');
            doc.setTextColor(107, 114, 128);
            doc.text('R.V. College of Engineering(R) • DTL Project 2026', 107.9, footerY + 12, { align: 'center' });
            
            doc.save(`BreathAnalysis_Report_${topClass}_${Date.now()}.pdf`);

        } catch (err) {
            showError(`Could not generate PDF report: ${err.message}`);
            console.error(err);
        } finally {
            btn.disabled = false;
            btn.innerHTML = originalText;
        }
    }

    function showError(message) {
        const existing = document.querySelector('.toast-error');
        if (existing) existing.remove();

        const toast = document.createElement('div');
        toast.className = 'toast-error';
        toast.setAttribute('role', 'alert');
        toast.innerHTML = `
            <span class="toast-icon">⚠️</span>
            <span class="toast-message">${escapeHTML(message)}</span>
            <button class="toast-close" aria-label="Close">✕</button>
        `;

        Object.assign(toast.style, {
            position: 'fixed',
            bottom: '24px',
            right: '24px',
            zIndex: '10000',
            display: 'flex',
            alignItems: 'center',
            gap: '12px',
            padding: '16px 20px',
            background: 'linear-gradient(135deg, #1e1b2e, #1a1425)',
            border: '1px solid rgba(239, 68, 68, 0.3)',
            borderRadius: '12px',
            color: '#fca5a5',
            fontSize: '14px',
            fontFamily: 'Inter, sans-serif',
            boxShadow: '0 8px 32px rgba(0,0,0,0.4)',
            transform: 'translateY(20px)',
            opacity: '0',
            transition: 'all 0.3s ease'
        });

        document.body.appendChild(toast);

        requestAnimationFrame(() => {
            toast.style.transform = 'translateY(0)';
            toast.style.opacity = '1';
        });

        toast.querySelector('.toast-close')?.addEventListener('click', () => removeToast(toast));

        setTimeout(() => removeToast(toast), 6000);
    }

    function removeToast(toast) {
        if (!toast || !toast.parentNode) return;
        toast.style.transform = 'translateY(20px)';
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 300);
    }

    function formatPlaybackTime(seconds) {
        const m = String(Math.floor(seconds / 60)).padStart(2, '0');
        const s = String(Math.floor(seconds) % 60).padStart(2, '0');
        return `${m}:${s}`;
    }

    function showPlayback(blob) {
        hidePlayback();
        const url = URL.createObjectURL(blob);
        playbackAudio = new Audio(url);

        playbackAudio.addEventListener('loadedmetadata', () => {
            const dur = playbackAudio.duration;
            if (dom.playbackTime) dom.playbackTime.textContent = `00:00 / ${formatPlaybackTime(dur)}`;
        });

        playbackAudio.addEventListener('ended', () => {
            cancelAnimationFrame(playbackRAF);
            if (dom.playbackIconPlay) dom.playbackIconPlay.style.display = '';
            if (dom.playbackIconPause) dom.playbackIconPause.style.display = 'none';
            if (dom.playbackProgressFill) dom.playbackProgressFill.style.width = '0%';
            if (dom.playbackTime) dom.playbackTime.textContent = `00:00 / ${formatPlaybackTime(playbackAudio.duration)}`;
        });

        if (dom.playbackSection) dom.playbackSection.style.display = 'block';

        dom.playbackBtn?.addEventListener('click', togglePlayback);

        dom.playbackProgressTrack?.addEventListener('click', (e) => {
            if (!playbackAudio || !playbackAudio.duration) return;
            const rect = dom.playbackProgressTrack.getBoundingClientRect();
            const ratio = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
            playbackAudio.currentTime = ratio * playbackAudio.duration;
            updatePlaybackProgress();
        });
    }

    function togglePlayback() {
        if (!playbackAudio) return;
        if (playbackAudio.paused) {
            playbackAudio.play();
            if (dom.playbackIconPlay) dom.playbackIconPlay.style.display = 'none';
            if (dom.playbackIconPause) dom.playbackIconPause.style.display = '';
            tickPlayback();
        } else {
            playbackAudio.pause();
            cancelAnimationFrame(playbackRAF);
            if (dom.playbackIconPlay) dom.playbackIconPlay.style.display = '';
            if (dom.playbackIconPause) dom.playbackIconPause.style.display = 'none';
        }
    }

    function tickPlayback() {
        updatePlaybackProgress();
        if (playbackAudio && !playbackAudio.paused) {
            playbackRAF = requestAnimationFrame(tickPlayback);
        }
    }

    function updatePlaybackProgress() {
        if (!playbackAudio || !playbackAudio.duration) return;
        const pct = (playbackAudio.currentTime / playbackAudio.duration) * 100;
        if (dom.playbackProgressFill) dom.playbackProgressFill.style.width = `${pct}%`;
        if (dom.playbackTime) dom.playbackTime.textContent = `${formatPlaybackTime(playbackAudio.currentTime)} / ${formatPlaybackTime(playbackAudio.duration)}`;
    }

    function hidePlayback() {
        if (playbackAudio) {
            playbackAudio.pause();
            playbackAudio = null;
        }
        cancelAnimationFrame(playbackRAF);
        if (dom.playbackSection) dom.playbackSection.style.display = 'none';
        if (dom.playbackProgressFill) dom.playbackProgressFill.style.width = '0%';
        if (dom.playbackIconPlay) dom.playbackIconPlay.style.display = '';
        if (dom.playbackIconPause) dom.playbackIconPause.style.display = 'none';
        dom.playbackBtn?.removeEventListener('click', togglePlayback);
    }

    function init() {
        initNavigation();
        initFileUpload();
        initMicrophone();
        initDiseaseCards();
        initModalTabs();
        initModalClose();
        initLearnMore();
        initDownloadReport();
        initScrollAnimations();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
