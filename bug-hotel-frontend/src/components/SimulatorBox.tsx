import '../App.css'

import Bug from './Bug.tsx'
import Hotel from './Hotel.tsx'
import {useState, useEffect, ReactElement} from 'react'
import {bugHashmap} from '../assets/static/Bugs.tsx'

import getQueueArray from '../Scripts/getQueueArray.ts'
import getHotelData from '../Scripts/getHotelData.ts'

type BugEl = {
  bug: string,
  x: number,
  y: number
}

const bugElements: BugEl[] = []

export default function Simulation() {
          const [spriteClock,setSpriteClock] = useState(0)
          useEffect(() => {
            const interval = setInterval(() => {
              if (spriteClock==0){
                setSpriteClock(1)
              } else {
                setSpriteClock(0)
              }
            }, 180)

            return () => clearInterval(interval)
          })
          const mappedBugElements:ReactElement[] = []
          for (const [key, value] of Object.entries(bugElements)) {
              mappedBugElements.push(<Bug spriteURL={bugHashmap[value.bug]} spriteClock={spriteClock} mode={0} x={value.x} y={value.y}/>);
          }
    return (
        <>
            <div id="simulatorBoxBlock" className="flex">
                <div id="simulatorBox">
                    <div id="background" className="sprite">
                        {mappedBugElements}
                        <Hotel/>
                    </div>
                </div>
            </div>
        </>
    )
}

interface addNewBugProps {
  uniqueID: number,
  bug: string,
  x: number,
  y: number
}

export function addNewBug({uniqueID,bug,x,y}:addNewBugProps) {
  bugElements[uniqueID]=({bug:bug,x:x,y:y})
} //When a bug first gets initialised in the Fast API code crew, this is what should eventually be called to visually represent them.

interface setBugIntegerVariableProps {
  uniqueID: number,
  variable: string,
  newValue: number,
}

export function setBugIntegerVariable({uniqueID,variable,newValue}:setBugIntegerVariableProps){
  bugElements[uniqueID][variable]=newValue
} //Function to control their movement, how they move is coded elsewhere.

export async function parseQueue(){
    const data = await getQueueArray()
    for (let i=0;i<data.length;i++){
        console.log(data[i])
    }
}

addNewBug({uniqueID:1,bug:"Caterpillar",x:0,y:0})
setBugIntegerVariable({uniqueID:1,variable:"x",newValue: 300})
setBugIntegerVariable({uniqueID:1,variable:"y",newValue: 350})
parseQueue()