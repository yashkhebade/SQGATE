(function() {
  function injectModal(msg, stack) {
    if (document.getElementById('sqgate-global-error-modal')) return;
    
    const style = document.createElement('style');
    style.textContent = `
      #sqgate-global-error-modal {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(10, 15, 30, 0.7); backdrop-filter: blur(10px);
        z-index: 9999999; display: flex; align-items: center; justify-content: center;
        font-family: 'Outfit', sans-serif; opacity: 0; transition: opacity 0.3s;
      }
      .sg-em-box {
        background: rgba(20, 25, 45, 0.8); border: 1px solid rgba(255,255,255,0.1);
        padding: 30px; border-radius: 12px; width: 90%; max-width: 500px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5); text-align: center; color: white;
      }
      .sg-em-icon { font-size: 40px; margin-bottom: 15px; }
      .sg-em-title { font-size: 24px; font-weight: 600; margin-bottom: 10px; color: #ff5555; }
      .sg-em-msg { font-size: 14px; margin-bottom: 25px; color: #b0b5c0; word-break: break-all; }
      .sg-em-actions { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; }
      .sg-em-btn {
        padding: 10px 20px; border-radius: 6px; cursor: pointer; border: none; font-weight: 500;
        text-decoration: none; display: inline-block; transition: all 0.2s; font-family: 'Outfit', sans-serif;
      }
      .sg-em-primary { background: #4f46e5; color: white; }
      .sg-em-primary:hover { background: #4338ca; }
      .sg-em-secondary { background: rgba(255,255,255,0.1); color: white; }
      .sg-em-secondary:hover { background: rgba(255,255,255,0.15); }
      .sg-em-dismiss { background: transparent; border: 1px solid rgba(255,255,255,0.2); color: #aaa; margin-top: 15px; width: 100%; }
      .sg-em-dismiss:hover { color: white; background: rgba(255,255,255,0.05); }
    `;
    document.head.appendChild(style);

    const modal = document.createElement('div');
    modal.id = 'sqgate-global-error-modal';
    
    // Safely encode msg to prevent XSS
    const safeMsg = String(msg).replace(/</g, '&lt;').replace(/>/g, '&gt;');
    
    modal.innerHTML = `
      <div class="sg-em-box">
        <div class="sg-em-icon">⚠️</div>
        <div class="sg-em-title">Application Error</div>
        <div class="sg-em-msg">${safeMsg}</div>
        <div class="sg-em-actions">
          <button class="sg-em-btn sg-em-primary" id="sg-em-report-btn">Report Bug (Auto)</button>
          <a class="sg-em-btn sg-em-secondary" href="https://docs.google.com/forms/d/e/1FAIpQLSc5AzzP2NccDkCbKAb5mVvefYFc5_X-EkJZx5RLWO7aqQ_8cw/viewform" target="_blank">Describe Bug in Detail</a>
        </div>
        <button class="sg-em-btn sg-em-dismiss" id="sg-em-dismiss-btn">Dismiss</button>
      </div>
    `;
    document.body.appendChild(modal);
    
    setTimeout(() => modal.style.opacity = '1', 10);
    
    document.getElementById('sg-em-dismiss-btn').onclick = () => {
      modal.style.opacity = '0';
      setTimeout(() => modal.remove(), 300);
    };
    
    document.getElementById('sg-em-report-btn').onclick = () => {
      const btn = document.getElementById('sg-em-report-btn');
      btn.textContent = 'Sending...';
      btn.style.opacity = '0.5';
      btn.disabled = true;
      
      fetch('http://localhost:8080/api/report-bug', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: msg, stack: stack, url: window.location.href })
      }).then(res => {
        if(res.ok) {
          btn.textContent = 'Sent Successfully!';
          btn.style.background = '#10b981';
          btn.style.opacity = '1';
        } else {
          btn.textContent = 'Failed to Send';
          btn.style.background = '#ef4444';
          btn.style.opacity = '1';
          btn.disabled = false;
        }
      }).catch(err => {
        btn.textContent = 'Network Error';
        btn.style.background = '#ef4444';
        btn.style.opacity = '1';
        btn.disabled = false;
      });
    };
  }

  window.addEventListener('error', function(event) {
    injectModal(event.message + ' at ' + event.filename + ':' + event.lineno, event.error ? event.error.stack : '');
  });
  
  window.addEventListener('unhandledrejection', function(event) {
    injectModal(event.reason, event.reason && event.reason.stack ? event.reason.stack : '');
  });
})();
