// @flow
import React from 'react'
import type { Community } from 'flow/types'
import { Entry, Error, Loading, Panel } from 'components'

type Props = {
  community: Community,
  isLoading: boolean,
  isError: boolean,
}

const CommunityPanel = (props: Props) => {
  const {community, isLoading, isError} = props
  const {name, latitude, longitude, size, installation, lastInspection} = community
  if (isLoading) {
    return <Loading />
  }
  else if (isError) {
    return <Error />
  }
  return (
    <Panel header={name}>
      <Entry>Latitude: {latitude}</Entry>
      <Entry>Longitude: {longitude}</Entry>
      <Entry>Size of community: {size} people</Entry>
      <Entry>Installation date: {installation.toString()}</Entry>
      <Entry>Last inspection date: {lastInspection.toString()}</Entry>
    </Panel>
  )
}

export default CommunityPanel
