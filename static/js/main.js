document.addEventListener('DOMContentLoaded', () => {
    // Theme toggling functionality
    const themeBtn = document.getElementById('theme-toggle-btn');
    if (themeBtn) {
        // Check saved theme
        const savedTheme = localStorage.getItem('theme') || 'light';
        document.documentElement.setAttribute('data-theme', savedTheme);
        themeBtn.innerHTML = savedTheme === 'dark' ? '☀️' : '🌓';

        themeBtn.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            themeBtn.innerHTML = newTheme === 'dark' ? '☀️' : '🌓';
        });
    }

    // Interactive OSI Layer Fetching
    const layerCards = document.querySelectorAll('.layer-card');
    const detailPanel = document.getElementById('detail-panel');
    const placeholder = document.querySelector('.panel-placeholder');
    const panelContent = document.getElementById('panel-content');

    if (layerCards.length > 0 && detailPanel) {
        layerCards.forEach(card => {
            card.addEventListener('click', async () => {
                // Formatting active state
                layerCards.forEach(c => c.classList.remove('selected'));
                card.classList.add('selected');

                const layerNumber = card.getAttribute('data-layer');
                try {
                    // Fetch data using AJAX without page reload
                    const response = await fetch(`/api/layer/${layerNumber}/`);
                    if (response.ok) {
                        const data = await response.json();

                        document.getElementById('pd-name').textContent = data.name;
                        document.getElementById('pd-num').textContent = `Layer ${data.layer_number}`;
                        document.getElementById('pd-desc').textContent = data.description;
                        document.getElementById('pd-example').textContent = data.real_life_example;
                        document.getElementById('pd-protocols').textContent = data.protocols;

                        placeholder.classList.add('hidden');
                        panelContent.classList.remove('hidden');
                    } else {
                        console.error('Layer not found');
                    }
                } catch (error) {
                    console.error('Network error fetching layer details:', error);
                }
            });
        });
    }

    // Protocol Explorer Filtering
    const protocolSearch = document.getElementById('search-input');
    const layerFilter = document.getElementById('layer-filter');
    const protocolList = document.getElementById('protocol-list');

    if (protocolSearch && layerFilter && protocolList) {
        const fetchProtocols = async () => {
            const query = protocolSearch.value;
            const layerId = layerFilter.value;

            try {
                const response = await fetch(`/protocols/api/protocols/?search=${encodeURIComponent(query)}&layer_id=${encodeURIComponent(layerId)}`);
                if (response.ok) {
                    const data = await response.json();

                    // Clear current list
                    protocolList.innerHTML = '';

                    // Add new rows
                    data.protocols.forEach(p => {
                        const tr = document.createElement('tr');
                        tr.innerHTML = `
                            <td><strong>${p.name}</strong></td>
                            <td><span class="badge">${p.layer_name}</span></td>
                            <td>${p.default_port || '-'}</td>
                            <td>${p.description}</td>
                        `;
                        protocolList.appendChild(tr);
                    });
                }
            } catch (error) {
                console.error('Error fetching protocols:', error);
            }
        };

        protocolSearch.addEventListener('input', fetchProtocols);
        layerFilter.addEventListener('change', fetchProtocols);
    }

    // Quiz Functionality
    const startBtn = document.getElementById('start-btn');
    if (startBtn) {
        let questions = [];
        let currentQuestionIndex = 0;
        let score = 0;
        let answered = false;

        const quizSetup = document.getElementById('quiz-setup');
        const quizArea = document.getElementById('quiz-area');
        const quizResults = document.getElementById('quiz-results');
        const optionBtns = document.querySelectorAll('.option-btn');
        const nextBtn = document.getElementById('next-btn');
        const explanationBox = document.getElementById('explanation-box');

        startBtn.addEventListener('click', async () => {
            startBtn.textContent = 'Loading...';
            startBtn.disabled = true;
            try {
                const response = await fetch('/quiz/api/questions/');
                if (response.ok) {
                    const data = await response.json();
                    questions = data.questions;

                    if (questions.length === 0) {
                        alert('No questions available yet! Please populate the database.');
                        startBtn.textContent = 'Start Quiz';
                        startBtn.disabled = false;
                        return;
                    }

                    startBtn.textContent = 'Start Quiz';
                    startBtn.disabled = false;
                    score = 0;
                    currentQuestionIndex = 0;

                    quizSetup.classList.add('hidden');
                    quizResults.classList.add('hidden');
                    quizArea.classList.remove('hidden');

                    loadQuestion();
                }
            } catch (err) {
                console.error(err);
                startBtn.textContent = 'Start Quiz';
                startBtn.disabled = false;
            }
        });

        function loadQuestion() {
            explained = false;
            answered = false;
            const q = questions[currentQuestionIndex];

            document.getElementById('current-question-num').textContent = currentQuestionIndex + 1;
            document.getElementById('score').textContent = score;
            document.getElementById('question-text').textContent = q.question;

            document.getElementById('opt-a-text').textContent = q.option_a;
            document.getElementById('opt-b-text').textContent = q.option_b;
            document.getElementById('opt-c-text').textContent = q.option_c;
            document.getElementById('opt-d-text').textContent = q.option_d;

            explanationBox.classList.add('hidden');

            optionBtns.forEach(btn => {
                btn.className = 'option-btn';
                btn.disabled = false;
            });
        }

        optionBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                if (answered) return;
                answered = true;

                const selectedChoice = btn.getAttribute('data-choice');
                const q = questions[currentQuestionIndex];
                const correctChoice = q.correct_answer;

                if (selectedChoice === correctChoice) {
                    btn.classList.add('correct');
                    score++;
                    document.getElementById('result-title').textContent = 'Correct!';
                    document.getElementById('result-title').style.color = '#22c55e';
                } else {
                    btn.classList.add('wrong');
                    document.getElementById('result-title').textContent = 'Incorrect!';
                    document.getElementById('result-title').style.color = '#ef4444';

                    // Highlight correct answer
                    optionBtns.forEach(ob => {
                        if (ob.getAttribute('data-choice') === correctChoice) {
                            ob.classList.add('correct');
                        }
                    });
                }

                document.getElementById('score').textContent = score;
                document.getElementById('explanation-text').textContent = q.explanation;
                explanationBox.classList.remove('hidden');

                optionBtns.forEach(ob => ob.disabled = true);
            });
        });

        nextBtn.addEventListener('click', () => {
            currentQuestionIndex++;
            if (currentQuestionIndex < questions.length) {
                loadQuestion();
            } else {
                quizArea.classList.add('hidden');
                quizResults.classList.remove('hidden');
                document.getElementById('final-score-val').textContent = score;
            }
        });

        document.getElementById('restart-btn').addEventListener('click', () => {
            quizResults.classList.add('hidden');
            quizSetup.classList.remove('hidden');
        });
    }
});
