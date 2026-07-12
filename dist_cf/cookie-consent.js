(function() {
  if (localStorage.getItem('sqgate_cookie_consent')) return;

  const banner = document.createElement('div');
  banner.id = 'sqgate-cookie-banner';
  banner.style.cssText = `
    position: fixed;
    bottom: 24px;
    left: 24px;
    right: 24px;
    max-width: 600px;
    margin: 0 auto;
    background: #121626;
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 12px 40px rgba(0,0,0,0.5);
    z-index: 999999;
    font-family: system-ui, -apple-system, sans-serif;
    color: #f1f5f9;
    display: flex;
    flex-direction: column;
    gap: 16px;
    transform: translateY(150%);
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  `;

  banner.innerHTML = `
    <div style="display: flex; align-items: flex-start; gap: 16px;">
      <div style="font-size: 24px;">🍪</div>
      <div>
        <div style="font-weight: 600; font-size: 16px; margin-bottom: 4px;">We Value Your Privacy</div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.5;">
          We use strictly necessary cookies to keep you logged in and save your projects. 
          We also use optional telemetry cookies to see how people use SQGATE, which helps us improve the app.
        </div>
      </div>
    </div>
    <div style="display: flex; justify-content: flex-end; gap: 12px; margin-top: 8px;">
      <button id="sqgate-cookie-decline" style="background: transparent; color: #94a3b8; border: 1px solid #334155; padding: 8px 16px; border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: 600; transition: all 0.2s;">Decline Optional</button>
      <button id="sqgate-cookie-accept" style="background: #4f46e5; color: white; border: none; padding: 8px 16px; border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: 600; transition: all 0.2s;">Accept All</button>
    </div>
  `;

  document.body.appendChild(banner);
  
  // Animate in
  setTimeout(() => { banner.style.transform = 'translateY(0)'; }, 500);

  document.getElementById('sqgate-cookie-decline').addEventListener('click', () => {
    localStorage.setItem('sqgate_cookie_consent', 'declined');
    banner.style.transform = 'translateY(150%)';
    setTimeout(() => banner.remove(), 400);
  });

  document.getElementById('sqgate-cookie-accept').addEventListener('click', () => {
    localStorage.setItem('sqgate_cookie_consent', 'accepted');
    banner.style.transform = 'translateY(150%)';
    setTimeout(() => banner.remove(), 400);
  });

  // Hover states
  document.getElementById('sqgate-cookie-decline').addEventListener('mouseover', function(){ this.style.color = 'white'; this.style.borderColor = '#64748b'; });
  document.getElementById('sqgate-cookie-decline').addEventListener('mouseout', function(){ this.style.color = '#94a3b8'; this.style.borderColor = '#334155'; });
  document.getElementById('sqgate-cookie-accept').addEventListener('mouseover', function(){ this.style.filter = 'brightness(1.1)'; });
  document.getElementById('sqgate-cookie-accept').addEventListener('mouseout', function(){ this.style.filter = 'brightness(1)'; });

})();
