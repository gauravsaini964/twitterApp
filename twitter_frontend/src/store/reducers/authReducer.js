import * as ACTION_TYPE from "../actions/types";

const initialState = {
  name: "",
  email: "",
  username: "",
  profile_pic: "",
};

const authReducer = (state = initialState, action) => {
  switch (action.type) {
    case ACTION_TYPE.SET_USER_INFO:
      return {
        ...state,
        name: action.payload.name,
        email: action.payload.email,
        username: action.payload.username,
        profile_pic: action.payload.pic,
      };

    default:
      return state;
  }
};

export default authReducer;
