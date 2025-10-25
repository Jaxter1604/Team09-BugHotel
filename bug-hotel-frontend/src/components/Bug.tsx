import '../App.css'

interface spriteProps {
    spriteURL: string;
    spriteClock: number; //0 or 1! 0 for Frame 1, 1 for Frame 2
    mode: number; //0 or 1! 0 for Idle, 1 for Walking
    x: number;
    y: number;
}

//SHOULD CHANGE BUG COMPONENT TO RECEIVE A BUG CLASS INSTEAD OF THESE VARIABLES IF POSSIBLE :0

export default function Bug({spriteURL, spriteClock, mode, x, y}: spriteProps) {
    const px:number=(35*2*(spriteClock))+(35*4*mode)
    console.log(px);
    return (
        <>
            <div style={{width: "35px", height: "35px"}}>
                    <div id="bugSprite" style={{right:x+"px",top:(421-y)+"px"}}>
                        <img src={spriteURL} id="bugImg" className="sprite" style={{right: px + 'px'}} />
                    </div>
            </div>
        </>
    )
}