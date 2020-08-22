import React from "react";
import { Icon } from "@fluentui/react/lib/Icon";
import { TextField, Persona, PersonaSize, CommandButton } from "@fluentui/react";
import faker from "faker";
import "./index.css";
import { useState } from "react";
import { useEffect } from "react";

import { TweetCard } from "../components";

function App() {
  const [imageUrl] = useState(faker.image.avatar());
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

  return (
    <div className='App'>
      <div className='main-content'>
        <div className='sidebar'>
          <div className='heading-container'>
            <Icon iconName='PencilReply' style={{ fontSize: 80, color: "#409fff" }} />
            <h1 className='heading'>tweet</h1>
          </div>
        </div>
        <div className='feed'>
          <div className='page-title ml20'>
            <Icon iconName='Home' style={{ fontSize: 25, color: "whitesmoke" }} />
            <h2 className='heading ml10'>Home</h2>
          </div>
          <div className='write-container ml20 mt20'>
            <Persona size={PersonaSize.large} imageUrl={imageUrl} />
            <TextField
              multiline
              resizable={false}
              style={{ width: 600, height: 80 }}
              placeholder='Let us know your thoughts...'
              onChange={onTweeting}
              maxLength='250'
            />
            <CommandButton
              iconProps={{ iconName: "Add" }}
              classname='ml10'
              text='Tweet'
              style={{ width: 70 }}
              disabled={tweetButtonDisabled}
            />
          </div>
          <hr />
          <div className='tweet-container mt40'>
            <TweetCard />
            <TweetCard />
            <TweetCard />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
