import './App.css'
import Bug from './components/Bug.tsx'
import {useState, useEffect} from 'react'

//All sprites
import ant from './assets/static/media/sprites/ant.png'
import beetle from './assets/static/media/sprites/beetle.png'
import fly from './assets/static/media/sprites/fly.png'
import worm from './assets/static/media/sprites/worm.png'
import bee from './assets/static/media/sprites/bee.png'
import wasp from './assets/static/media/sprites/wasp.png'
import caterpiller from './assets/static/media/sprites/caterpiller.png'
import butterfly from './assets/static/media/sprites/butterfly.png'
import moth from './assets/static/media/sprites/moth.png'
import grasshopper from './assets/static/media/sprites/grasshopper.png'
import mosquito from './assets/static/media/sprites/mosquito.png'
import spider from './assets/static/media/sprites/spider.png'

function App() {
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
      <p>i lvoe bug ho tel!!!!!!</p>
      <Bug spriteURL={ant} spriteClock={spriteClock} mode={0} />
      <Bug spriteURL={beetle} spriteClock={spriteClock} mode={0} />
      <Bug spriteURL={fly} spriteClock={spriteClock} mode={0} />
      <Bug spriteURL={worm} spriteClock={spriteClock} mode={0} />
      <Bug spriteURL={bee} spriteClock={spriteClock} mode={0} />
      <Bug spriteURL={wasp} spriteClock={spriteClock} mode={0} />
      <Bug spriteURL={caterpiller} spriteClock={spriteClock} mode={0} />
      <Bug spriteURL={butterfly} spriteClock={spriteClock} mode={0} />
      <Bug spriteURL={moth} spriteClock={spriteClock} mode={0} />
      <Bug spriteURL={grasshopper} spriteClock={spriteClock} mode={0} />
      <Bug spriteURL={mosquito} spriteClock={spriteClock} mode={0} />
      <Bug spriteURL={spider} spriteClock={spriteClock} mode={0} />
    </>
  )
}

export default App
