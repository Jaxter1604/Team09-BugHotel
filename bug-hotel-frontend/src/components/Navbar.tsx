import '../App.css'
import bugHotelLogo from '../assets/static/media/bugHotelLogo.png'
import DYHTG from '../assets/static/media/DYHTG.png'


export default function Navbar() {
    return (
        <>
            <div id="navbar" className="flex">
                <div id="navbarBox" className="flex">
                    <img id="navbarBugLogo" src={bugHotelLogo}/>
                    <p id="navbarText">Made for DYHTG Hackathon 2025 - Morgan Stanley Challenge, by Team 9!</p>
                    <img id="navbarBugLogo" src={DYHTG}/>
                </div>
            </div>
        </>
    )
}