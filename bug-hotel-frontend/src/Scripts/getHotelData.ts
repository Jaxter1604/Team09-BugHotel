export default async function getHotelJSON() {
    let response = await fetch("http://localhost:8000/hotel");

    if (!response.ok) {
        throw new Error(`Response status ${response.status}`);
    }

    const hotelData = await response.json();
    return hotelData;    
}

console.log(await getHotelJSON())