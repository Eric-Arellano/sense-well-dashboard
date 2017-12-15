// @flow
import React from 'react'
import { Footer, Header } from 'components'
import s from './App.module.css'
import { DashboardViewContainer } from 'containers'

type Props = {}

const App = (props: Props) => {

  return (
    <div className={s.app}>
      <Header />
      <div className={s.body}>
        <DashboardViewContainer />
      </div>
      <Footer />
    </div>
  )
}

export default App