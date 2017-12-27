import React from 'react'
import { Error, Loading } from 'components'

// tutorial at https://medium.com/@shaun_gallagher/use-a-decorator-to-conditionally-render-react-components-da80b27a3ebf
// - target = React component
// - descriptor.value = method being decorated (i.e. render() function)

// Call this decorator on render() function.
// Class must have isError and isLoading state value and resetState as class property.
const withLoadingAndError = (errorMessage: string) => (target, key, descriptor) => {
  target.renderOnLoad = target.renderOnLoad || descriptor.value
  descriptor.value = function () {
    const render = target.renderOnLoad.bind(this)
    const {isError, isLoading} = this.state
    const {resetState} = this
    if (isError) {
      return <Error resetState={resetState}>{errorMessage}</Error>
    } else if (isLoading) {
      return <Loading />
    }
    return render()
  }
  return descriptor
}

export default withLoadingAndError