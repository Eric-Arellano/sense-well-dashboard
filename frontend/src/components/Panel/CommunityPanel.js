// @flow
import React from 'react'
import type { Community } from 'flow/types'
import Entry from './Entry'
import s from './Panel.module.css'

type Props = {
  community: Community,
}

const CommunityPanel = (props: Props) => {
  const {name, latitude, longitude, size, installation, lastInspection} = props.community
  return (
    <div className={s.container}>
      <h1 className={s.header}>{name}</h1>
      <div className={s.body}>
        <Entry>Latitude: {latitude}</Entry>
        <Entry>Longitude: {longitude}</Entry>
        <Entry>Size of community: {size} people</Entry>
        <Entry>Installation date: {installation.toString()}</Entry>
        <Entry>Last inspection date: {lastInspection.toString()}</Entry>
      </div>
    </div>
  )
}

export default CommunityPanel
