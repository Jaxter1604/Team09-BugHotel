import '../App.css'
import Bug from '../components/Bug.tsx'
import {useState, useEffect} from 'react'

import Simulation from '../components/SimulatorBox.tsx'

//All sprites
import ant from '../assets/static/media/sprites/ant.png'
import beetle from '../assets/static/media/sprites/beetle.png'
import fly from '../assets/static/media/sprites/fly.png'
import worm from '../assets/static/media/sprites/worm.png'
import bee from '../assets/static/media/sprites/bee.png'
import wasp from '../assets/static/media/sprites/wasp.png'
import caterpiller from '../assets/static/media/sprites/caterpiller.png'
import butterfly from '../assets/static/media/sprites/butterfly.png'
import moth from '../assets/static/media/sprites/moth.png'
import grasshopper from '../assets/static/media/sprites/grasshopper.png'
import mosquito from '../assets/static/media/sprites/mosquito.png'
import spider from '../assets/static/media/sprites/spider.png'

export default function Main() {
      const [spriteClock,setSpriteClock] = useState(0)
      useEffect(() => {
        const interval = setInterval(() => {
          if (spriteClock==0){
            setSpriteClock(1)
          } else {
            setSpriteClock(0)
          }
        }, 200)
    
        return () => clearInterval(interval)
      })
    return (
        <>
            <Simulation/>
        </>
    )
}