import { useState } from 'react'
import HomePage from './components/HomePage.tsx'
import CreatePage from './components/CreatePage.tsx'

import './App.css'

function App() {
  const [mainView, setMainView] = useState<'home' | 'create'>('home')

  return (
    <>
      {mainView === 'home' && <HomePage onCreateClick={() => setMainView('create')}/>}
      {mainView === 'create' && <CreatePage onBackClick={() => setMainView('home')} />}
    </>
  )
}

export default App
