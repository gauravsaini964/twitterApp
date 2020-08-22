import * as ACTION_TYPE from "./types";

export const setUserInfo = (payload) => (dispatch) => {
  dispatch({ type: ACTION_TYPE.SET_USER_INFO, payload });
};
