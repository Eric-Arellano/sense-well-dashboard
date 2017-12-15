// @flow
import * as React from 'react'

type Props = {
  children: React.Element<string>  // can only be a single child of type string
}

const Entry = (props: Props) => {
  return (
    <p>{props.children}</p>
  )
}

export default Entry