import '../App.css'
import bugHotelLogo from '../assets/static/media/bugHotelLogo.png'
import DYHTG from '../assets/static/media/DYHTG.png'


export default function Navbar() {
    return (
        <>
            <div id="navbar" className="flex">
                <div id="navbarBox" className="flex">
                    <img id="navbarBugLogo" src={bugHotelLogo}/>
                    <img id="navbarBugLogo" src={DYHTG}/>
                </div>
            </div>
        </>
    )
}