import React from "react";
import { loadTheme, initializeIcons, Spinner, SpinnerSize } from "@fluentui/react";
import { theme } from "./theme";
import { connect } from "react-redux";
import Screen from "./screens/Feed";
import faker from "faker";
import { authAPI } from "./utilities/api";
import { setUserInfo } from "./store/actions";

class App extends React.PureComponent {
  constructor(props) {
    super(props);
    loadTheme(theme);
    initializeIcons();
  }

  state = { isLoading: true };

  componentWillMount = async () => {
    if (!localStorage.getItem("token")) {
      const authData = {
        email: faker.internet.email(),
        first_name: faker.name.firstName(),
        last_name: faker.name.lastName(),
        profile_pic: faker.image.avatar(),
      };
      const { data, statusCode } = await authAPI.post("/v1/auth/", authData);
      if (statusCode === 201 || statusCode === 200) {
        localStorage.setItem("token", `Bearer ${data.result.token}`);
        this.props.setUserInfo(data.result);
        this.setState({ isLoading: false });
      } else {
        alert("Something went wrong");
        this.setState({ isLoading: false });
      }
    } else {
      const { data, statusCode } = await authAPI.post("/v1/login/");
      if (statusCode === 200) {
        this.setState({ isLoading: false });
        this.props.setUserInfo(data.result);
      } else {
        localStorage.clear();
        alert("Something went wrong");
      }
    }
  };

  render() {
    return <>{this.state.isLoading ? <Spinner size={SpinnerSize.large} /> : <Screen />}</>;
  }
}

const wrappedApp = connect(null, { setUserInfo })(App);

export default wrappedApp;
