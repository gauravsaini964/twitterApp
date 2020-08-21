import React from "react";
import { loadTheme, initializeIcons } from "@fluentui/react";
import { theme } from "./theme";
import Screen from "./screens";

class App extends React.PureComponent {
  constructor(props) {
    super(props);
    loadTheme(theme);
    initializeIcons();
  }

  render() {
    return (
      <>
        <Screen />
      </>
    );
  }
}

export default App;
