export interface Evento {
  id: string;
  name: string;
  date: string;
  description: string;
  lat: number;
  lng: number;
  timestamp?: number;
}

export const EVENTS_DATA: Evento[] = [
  { id: 'ev-1', name: 'Reyes / Romería local', date: '6 Enero, 2026', description: 'Cabalgata, ambiente familiar y misa. Tarde tranquila con recogida de caramelos.', lat: 42.3260, lng: -8.7850 },
  { id: 'ev-2', name: 'Trail / Caminata en Cela', date: '19 Enero (Aprox.)', description: 'Evento deportivo de monte en Cela. Carrera por senderos, bosques y costa. Buen ambiente con tapeo.', lat: 42.3420, lng: -8.7900 },
  { id: 'ev-3', name: 'Festival de comparsas (Bueu)', date: '20 Febrero, 2026', description: 'Humor, coreografías y crítica en grupos disfrazados. Mucha gente joven y bares llenos.', lat: 42.3260, lng: -8.7850 },
  { id: 'ev-4', name: 'Festival de comparsas (Beluso)', date: '27 Febrero, 2026', description: 'Comparsas del pueblo. Ambiente más «de casa» que en Bueu pero muy animado.', lat: 42.3315, lng: -8.8160 },
  { id: 'ev-5', name: 'Entroido', date: 'Febrero (Fin de semana central)', description: 'Disfraces por la calle, desfiles, música y fiesta nocturna. De lo mejor del invierno.', lat: 42.3260, lng: -8.7850 },
  { id: 'ev-6', name: 'Enterro do Paxaro de Mal Agoiro', date: 'Marzo (Domingo)', description: 'Cierre del carnaval. Tradicional «entierro simbólico» y desfile con humor y sátira.', lat: 42.3260, lng: -8.7850 },
  { id: 'ev-7', name: 'Milla da Muller', date: '8-16 Marzo', description: 'Carreras populares y eventos deportivos por el Día de la Mujer en Bueu. Ambiente familiar.', lat: 42.3260, lng: -8.7850 },
  { id: 'ev-8', name: 'Evento en la Isla de Ons', date: '27 Abril (Aprox.)', description: 'Carrera o ruta de senderismo en la isla. Paisajes espectaculares y planazo de excursión diurna.', lat: 42.3800, lng: -8.9330 },
  { id: 'ev-9', name: 'Mes del Pulpo', date: '10-24 Mayo', description: 'Jornadas gastronómicas en Bueu. Restaurantes ofreciendo pulpo todo el mes, plan perfecto para tapear.', lat: 42.3260, lng: -8.7850 },
  { id: 'ev-10', name: 'Corpus Christi', date: '25 Mayo, 2026', description: 'Alfombras florales en las calles, procesión religiosa y mucha participación vecinal.', lat: 42.3260, lng: -8.7850 },
  { id: 'ev-11', name: 'San Antonio (Meiro)', date: '13-14 Junio', description: 'Fiesta típica de parroquia en Meiro. Orquestas, verbena nocturna y muy buen rollo.', lat: 42.3160, lng: -8.7800 },
  { id: 'ev-12', name: 'Noche de San Xoán', date: '23 Junio', description: 'Hogueras en playas, salto de fuego y fiesta fuerte con mucha gente joven.', lat: 42.3315, lng: -8.8160 },
  { id: 'ev-13', name: 'Día de San Juan', date: '24 Junio', description: 'Día relajado post-San Xoán. Ambiente de playa y bares post-hogueras.', lat: 42.3315, lng: -8.8160 },
  { id: 'ev-14', name: 'Festa do Viño', date: '8 Julio, 2026', description: 'Evento gastronómico en Bueu con vino local, tapas y pequeños conciertos.', lat: 42.3260, lng: -8.7850 },
  { id: 'ev-15', name: 'Virxe do Carme', date: '16 Julio, 2026', description: 'Procesión marítima con barcos, fuegos artificiales y orquestas grandes por la noche.', lat: 42.3260, lng: -8.7850 },
  { id: 'ev-16', name: 'SonRías Baixas', date: '31 Julio - 3 Agosto', description: 'Festivalazo de música en Bueu. Conciertos potentes, zona food trucks y mucha fiesta.', lat: 42.3260, lng: -8.7850 },
  { id: 'ev-17', name: 'Festa do Polbo', date: '10 Agosto, 2026', description: 'Fiesta del pulpo en Bueu con pasacalles y pulpo á feira en puestos. Gran ambiente.', lat: 42.3260, lng: -8.7850 },
  { id: 'ev-18', name: 'Fiestas de Beluso', date: '14-16 Agosto', description: 'Fiesta grande local con orquestas potentes (Panorama, etc.). Juegos, pasacalles y verbena.', lat: 42.3315, lng: -8.8160 },
  { id: 'ev-19', name: 'Fiestas de Cela', date: '15-17 Agosto', description: 'Patronales con verbenas, música y barracas para San Roque y Santa María.', lat: 42.3420, lng: -8.7900 },
  { id: 'ev-20', name: 'FICBUEU', date: '5-20 Septiembre', description: 'Festival Internacional de Cine en Bueu con proyecciones de cortos y charlas culturales.', lat: 42.3260, lng: -8.7850 },
  { id: 'ev-21', name: 'Festa do Cabalo + Dolores', date: '16-18 Octubre', description: 'Exhibiciones de caballos y concurso ecuestre. Tradición curiosa y algo de verbena en Beluso.', lat: 42.3315, lng: -8.8160 },
  { id: 'ev-22', name: 'Samaín', date: '31 Octubre', description: 'Versión gallega de Halloween con calabazas, disfraces, actividades infantiles y fiestas de noche.', lat: 42.3260, lng: -8.7850 },
  { id: 'ev-23', name: 'San Martiño', date: '11 Noviembre', description: 'Magosto tradicional (castañas y vino). Música y ambiente de pueblo muy típico.', lat: 42.3260, lng: -8.7850 }
];
