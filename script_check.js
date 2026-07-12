  console.log("shareCircuit button clicked!");
  try {
    const snap = projDataSnapshot();
    const jsonStr = JSON.stringify({name: PROJ ? PROJ.name : 'Shared Circuit', data: snap});
    
    // We do not encodeURIComponent here, btoa works fine with ascii from stringify
    // except stringify might have non-ascii. We use a safe base64 encoding method:
    const safeJson = unescape(encodeURIComponent(jsonStr));
    const b64 = btoa(safeJson);
    
    const url = window.location.origin + window.location.pathname + '#load=' + b64;
    
    document.getElementById('share-url-input').value = url;
    document.getElementById('share-modal').classList.add('show');
    document.getElementById('share-copy-btn').textContent = "Copy Link";
  } catch (err) {
    console.error("Failed to generate share link:", err);
    document.getElementById('share-url-input').value = "Error generating link: " + err.message;
    document.getElementById('share-modal').classList.add('show');
    document.getElementById('share-copy-btn').textContent = "Failed";
  }
}

function copyShareUrl() {
  const input = document.getElementById('share-url-input');
  input.select();
  input.setSelectionRange(0, 99999);
  try {
    document.execCommand('copy');
    document.getElementById('share-copy-btn').textContent = "Copied!";
  } catch(e) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(input.value).then(() => {
        document.getElementById('share-copy-btn').textContent = "Copied!";
      });
    }
  }
}

window.addEventListener('DOMContentLoaded', () => {
  if (window.location.hash.startsWith('#load=')) {
    try {
      const b64 = window.location.hash.substring(6);
      const decodedStr = decodeURIComponent(escape(atob(b64)));
      const sharedData = JSON.parse(decodedStr);
      
      setTimeout(() => {
        openProject({
          id: genId(),
          name: sharedData.name || 'Shared Circuit',
          data: sharedData.data
        });
        msg("Loaded shared circuit successfully!", "ok");
        history.replaceState(null, null, window.location.pathname);
      }, 300);
    } catch(err) {
      console.error("Failed to load shared circuit", err);
      // Fallback in case they used the old link format
      try {
        const jsonStr = decodeURIComponent(atob(window.location.hash.substring(6)));
        const sharedData = JSON.parse(jsonStr);
        setTimeout(() => {
          openProject({ id: genId(), name: sharedData.name, data: sharedData.data });
          msg("Loaded shared circuit successfully!", "ok");
          history.replaceState(null, null, window.location.pathname);
        }, 300);
      } catch(e2) {}
    }
  }
});
</script>
