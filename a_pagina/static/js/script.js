const WS = new WebSocket(`ws://${window.location.host}/ws/ticket/`);

WS.onopen = () => {
    console.log('Conectado al servidor de WebSocket');
};
const LISTA_PATHS = ['/', '/cocina/','/tabla-pendientes/','/tabla-delivery/','/tabla-todos/','/tabla-cobrado/','/ver-tabla-por-mesa/','/ver-tabla-por-mesa/[0-9]+/'];
WS.onmessage = (e) => {
    const data = JSON.parse(e.data);
    const ACCIONES_PERMITIDAS = ['created', 'deleted', 'updated'];
    if (LISTA_PATHS.includes(window.location.pathname) && ACCIONES_PERMITIDAS.includes(data.action)) {
        window.location.reload();
    }
};
