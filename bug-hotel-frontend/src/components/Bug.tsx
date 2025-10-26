import '../App.css'
import {useEffect,useRef} from 'react'

interface spriteProps {
    spriteURL: string;
    spriteClock: number; //0 or 1! 0 for Frame 1, 1 for Frame 2
    mode: number; //0 or 1! 0 for Idle, 1 for Walking
    x: number;
    y: number;
}

const yOffset:number=421
const speed:number=10

//SHOULD CHANGE BUG COMPONENT TO RECEIVE A BUG CLASS INSTEAD OF THESE VARIABLES IF POSSIBLE :0


export default function Bug({spriteURL, spriteClock, mode, x, y}: spriteProps) {
    const newx=useRef(-1)
    const newy=useRef(-1)

    var scaleVal:string="scale(1)"

    useEffect(() => {
        //Just created, initialise and don't edit until x or y is different
        if (newx.current==-1 || newy.current==-1) {
            if (newx.current==-1){
                newx.current=(x)
                console.log("First1")
            }
            if (newy.current==-1){
                newy.current=(yOffset-y)
                console.log("First2")
            }
        } else {
        //System to move bugs incremently to new x,y coordinate. First go to x coordinate then y coordinate.
            if (newy.current>yOffset-y) {
                scaleVal="scale(-1,1)"
                mode=1
                console.log("d")
                if ((newy.current-speed)<yOffset-y){
                    newy.current=(yOffset-y)
                } else {
                    newy.current=(newy.current-speed)
            }} else if (newx.current<x){
                mode=1
                scaleVal="scale(1)"
                console.log("a")
                if ((newx.current+speed)>x){
                    newx.current=(x)
                } else {
                    newx.current=(newx.current+speed)
                }
            } else if (newx.current>x) {
                mode=1
                scaleVal="scale(-1,1)"
                console.log("b")
                if ((newx.current-speed)<x){
                    newx.current=(x)
                } else {
                    newx.current=(newx.current-speed)
                }
            } else if (newy.current<yOffset-y){
                scaleVal="scale(1)"
                mode=1
                console.log("c")
                if ((newy.current+speed)>yOffset-y){
                    newy.current=(yOffset-y)
                } else {
                    newy.current=(newy.current+speed)
                }
            }
        }
    });
    console.log(scaleVal)
    const px:number=(35*2*(spriteClock))+(35*4*mode)
    return (
        <>
            <div style={{width: "35px", height: "35px"}}>
                    <div id="bugSprite" style={{right:newx.current+"px",top:newy.current+"px",transform:scaleVal}}>
                        <img src={spriteURL} id="bugImg" className="sprite" style={{right: px + 'px'}} />
                    </div>
            </div>
        </>
    )
}