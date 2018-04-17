// @flow
import React from 'react'
import { Footer, Header } from 'components'
import { DashboardContainer } from 'views'
import type { Community } from 'types'
import s from './App.module.css'

type Props = {
  community: Community
}

const App = ({ community }: Props) => {
  return (
    <div className={s.app}>
      <Header />
      <main className={s.body}>
        <DashboardContainer community={community} />
      </main>
      <Footer />
    </div>
  )
}

export default App
