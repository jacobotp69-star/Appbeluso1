export type POICategory = 'playa' | 'restaurante' | 'museo' | 'inicio' | 'generico' | 'senderos' | 'pesca' | 'urgencias' | 'alquiler';

export interface POI {
  id: string;
  lat: number;
  lng: number;
  name: string;
  description: string;
  category: POICategory;
  imgUrl?: string;
  imgUrls?: string[];
  vidUrl?: string;
  isInitial?: boolean;
}
