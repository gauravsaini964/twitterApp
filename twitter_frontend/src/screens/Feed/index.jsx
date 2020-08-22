import React from "react";
import { Icon } from "@fluentui/react/lib/Icon";
import { TextField, Persona, PersonaSize, CommandButton } from "@fluentui/react";
import "./index.css";
import { useState } from "react";
import { useEffect } from "react";

import TweetList from "./MainContent/Tweets";
import { postTweet } from "../../store/actions";
import { useSelector, useDispatch } from "react-redux";

function App() {
  const dispatch = useDispatch();
  const userAuth = useSelector((state) => state.authReducer);
  const [tweet, setTweet] = useState("");
  const [tweetButtonDisabled, setTweetButtonDisabled] = useState(true);

  useEffect(() => {}, []);

  const onTweeting = (e, value) => {
    if (value) {
      setTweetButtonDisabled(false);
    } else {
      setTweetButtonDisabled(true);
    }
    setTweet(value);
  };

  const onTweetPostButtonPress = () => {
    const formData = { tweet };
    dispatch(postTweet(formData));
  };

  const renderContent = () => {
    return (
      <div className='main-content'>
        <div className='feed'>
          <div className='page-title ml20'>
            <Icon iconName='Home' style={{ fontSize: 25, color: "whitesmoke" }} />
            <h2 className='heading ml10'>Home</h2>
          </div>
          <div className='write-container ml10 mt20'>
            <Persona size={PersonaSize.large} imageUrl={userAuth.profile_pic} />
            <TextField
              multiline
              resizable={false}
              style={{ width: 575, height: 80 }}
              placeholder={`Hey ${userAuth.name}, Let us know your thoughts..`}
              onChange={onTweeting}
              maxLength='250'
            />
            <CommandButton
              iconProps={{ iconName: "Add" }}
              classname='ml10'
              text='Tweet'
              style={{ width: 70 }}
              disabled={tweetButtonDisabled}
              onClick={onTweetPostButtonPress}
            />
          </div>
          <hr />
          <div style={{ backgroundColor: "#222222", height: 10 }}></div>
          <div className='tweet-container'>
            <TweetList />
          </div>
        </div>
      </div>
    );
  };

  return <div className='App'>{renderContent()}</div>;
}

export default App;
