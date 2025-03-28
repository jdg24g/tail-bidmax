const WS = new WebSocket(`ws://${window.location.host}/ws/ticket/`);

WS.onopen = () => {
  console.log("Conectado al servidor de WebSocket");
};

const LISTA_PATHS = [
  "/",
  "/cocina/",
  "/tabla-pendientes/",
  "/tabla-delivery/",
  "/tabla-todos/",
  "/tabla-cobrado/",
  "/ver-tabla-por-mesa/",
];

WS.onmessage = (e) => {
  const data = JSON.parse(e.data);
  const ACCIONES_PERMITIDAS = ["created", "deleted", "updated"];

  // Verifica si la URL está en la lista de rutas exactas
  const esRutaExacta = LISTA_PATHS.includes(window.location.pathname);

  // Verifica si la URL coincide con el patrón /ver-tabla-por-mesa/{numero}/
  const regex = /^\/ver-tabla-por-mesa\/\d+\/$/;
  const esRutaDinamica = regex.test(window.location.pathname);

  if ((esRutaExacta || esRutaDinamica) && ACCIONES_PERMITIDAS.includes(data.action)) {
    window.location.reload();
  }
};
