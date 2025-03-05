const WS = new WebSocket(`ws://${window.location.host}/ws/ticket/`);

WS.onopen = () => {
    console.log('Conectado al servidor de WebSocket');
};

WS.onmessage = (e) => {
    const data = JSON.parse(e.data);
    if (window.location.pathname === '/' && data.action === "created") {
        window.location.reload();
    }
    else if (window.location.pathname === '/' && data.action === "deleted") {
        window.location.reload();
    }
    else if (window.location.pathname === '/' && data.action === "updated") {
        window.location.reload();
    }
};
