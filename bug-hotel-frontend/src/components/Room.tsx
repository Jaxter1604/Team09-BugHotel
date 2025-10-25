import '../App.css'

//80x65

import room from '../assets/static/media/room.png'
import {useState, useEffect} from 'react'

interface spriteProps {
    x: number;
    y: number;
}

export default function Room({x,y}:spriteProps) {
    return (
        <>
            <div style={{width: "80px", height: "65px"}}>
                <div id="room" style={{right:x+"px",top:(456-y)+"px"}}>
                    <img src={room} className="sprite"/>
                </div>
            </div>
        </>
    )
}