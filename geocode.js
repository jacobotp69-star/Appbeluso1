async function geocode(query) {
  const url = `https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(query)}&format=json&limit=1`;
  const res = await fetch(url, {
    headers: {
      'User-Agent': 'AppBeluso-Crawler/1.0 (jacob@appbeluso.com)'
    }
  });
  const data = await res.json();
  if (data.length > 0) {
    return { lat: parseFloat(data[0].lat), lng: parseFloat(data[0].lon) };
  }
  return null;
}

const places = [
  "A Meudina, Beluso, Bueu",
  "Taperia A Meudina, Beluso, Bueu",
  "Restaurante A Centoleira, Beluso, Bueu",
  "Restaurante Peixoto, Beluso, Bueu",
  "Cabo Udra, Bueu, Galicia",
  "Praia de Tuia, Bueu, Galicia",
  "Museo Masso, Bueu",
  "Praia de Pedron, Bueu",
  "Praia de Sartaxens, Bueu",
  "Area de Bon, Bueu",
  "Igrexa de Santa Maria de Beluso, Bueu",
  "Praia de Lagos, Bueu",
  "Praia de Ancoradoiro, Bueu",
  "Humedal de Escorregadoiro",
  "Capela dos Santos Reis, Bueu",
  "Praia da Mourisca, Bueu",
  "Praia da Roiba, Bueu",
  "Praia de Beluso, Bueu",
  "Porto de Beluso, Bueu",
  "Club Nautico Beluso, Bueu"
];

async function main() {
  for (const place of places) {
    const coords = await geocode(place);
    console.log(`${place}:`, coords);
    await new Promise(r => setTimeout(r, 1500)); // Respect Nominatim guidelines
  }
}

main();
