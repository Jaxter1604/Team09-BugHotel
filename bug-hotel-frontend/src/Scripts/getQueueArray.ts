export default async function getQueueArray() {
    let response = await fetch("/queue");

    if (!response.ok) {
        throw new Error(`Response status ${response.status}`);
    }

    const queueData = await response.json();
    return queueData["queue"];    
}