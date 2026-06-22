document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const loading = document.getElementById('loading');
    const welcome = document.getElementById('welcome');
    const results = document.getElementById('results');

    // UI Elements for data
    const summaryText = document.getElementById('summary-text');
    const financialsList = document.getElementById('financials-list');
    const legalList = document.getElementById('legal-list');
    const roadmapList = document.getElementById('roadmap-list');
    const tipsList = document.getElementById('tips-list');

    const handleSend = async () => {
        const query = userInput.value.trim();
        if (!query) return;

        // Show loading state
        userInput.disabled = true;
        sendBtn.style.display = 'none';
        loading.style.display = 'flex';

        try {
            const response = await fetch('/api/query', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query })
            });

            if (!response.ok) throw new Error('API Error');

            const data = await response.json();
            renderResults(data);
        } catch (error) {
            console.error(error);
            alert('Something went wrong. Please try again.');
        } finally {
            userInput.disabled = false;
            userInput.value = '';
            sendBtn.style.display = 'flex';
            loading.style.display = 'none';
        }
    };

    const renderResults = (data) => {
        // Hide welcome, show results
        welcome.style.display = 'none';
        results.style.display = 'block';

        // Summary
        summaryText.textContent = data.summary;

        // Financials
        financialsList.innerHTML = data.financial_requirements.map(req => `
            <div class="req-item">
                <span class="title">${req.item}</span>
                <span class="desc">${req.description} ${req.estimated_cost ? `(<strong>${req.estimated_cost}</strong>)` : ''}</span>
            </div>
        `).join('');

        // Legal
        legalList.innerHTML = data.legal_requirements.map(req => `
            <div class="req-item">
                <span class="title">${req.document}</span>
                <span class="desc">${req.description}</span>
            </div>
        `).join('');

        // Roadmap
        roadmapList.innerHTML = data.roadmap
            .sort((a, b) => a.order - b.order)
            .map(step => `
            <div class="step">
                <h4>${step.title}</h4>
                <p class="desc">${step.action}</p>
            </div>
        `).join('');

        // Tips
        tipsList.innerHTML = data.additional_tips.map(tip => `
            <li style="margin-bottom: 0.5rem; color: var(--text-muted);">✨ ${tip}</li>
        `).join('');

        // Scroll to results
        results.scrollIntoView({ behavior: 'smooth' });
    };

    sendBtn.addEventListener('click', handleSend);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleSend();
    });
});
