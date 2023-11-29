import React from 'react'

import styles from './thumbnail.module.css'

const Thumbnail = (props) => {
  return (
    <div className={styles['container']}>
      <div className={styles['thumbnail']}>
        <div className={styles['frame4']}>
          <div className={styles['frame41']}>
            <div className={styles['frame42']}>
              <span className={styles['text']}>
                <span>Online Academy</span>
              </span>
              <div className={styles['frame5']}>
                <span className={styles['text02']}>
                  <span>Revolutionizing the way we Learn with AI</span>
                </span>
                <span className={styles['text04']}>
                  <span>
                    Gain personalized study plans and improve progress through
                    BigBrainKids. Familiarize yourself with AI.
                    <span
                      dangerouslySetInnerHTML={{
                        __html: ' ',
                      }}
                    />
                  </span>
                </span>
              </div>
            </div>
            <div className={styles['frame7']}>
              <span className={styles['text06']}>
                <span>Sign In →</span>
              </span>
              <div className={styles['frame2']}>
                <span className={styles['text08']}>
                  <span>Learn more →</span>
                </span>
              </div>
            </div>
          </div>
          <div className={styles['frame8']}>
            <div className={styles['frame3']}>
              <img
                alt="Frame32101"
                src="/frame32101-4ud.svg"
                className={styles['frame31']}
              />
              <span className={styles['text10']}>
                <span>Hours of content</span>
              </span>
            </div>
            <img
              alt="Vector12101"
              src="/vector12101-8bz.svg"
              className={styles['vector1']}
            />
            <div className={styles['frame32']}>
              <img
                alt="Frame82101"
                src="/frame82101-5p1r.svg"
                className={styles['frame81']}
              />
              <span className={styles['text12']}>
                <span>Active Users</span>
              </span>
            </div>
          </div>
        </div>
        <div className={styles['frame82']}>
          <div className={styles['frame51']}>
            <span className={styles['text14']}>
              <span>BigBrainKids</span>
            </span>
            <img
              alt="Vector12101"
              src="/vector12101-l83.svg"
              className={styles['vector11']}
            />
            <span className={styles['text16']}>
              <span>Main</span>
            </span>
            <span className={styles['text18']}>
              <span>Guide</span>
            </span>
            <span className={styles['text20']}>
              <span>Statistics</span>
            </span>
            <div className={styles['frame33']}>
              <span className={styles['text22']}>
                <span>Games</span>
              </span>
              <img
                alt="Frame82101"
                src="/frame82101-6xs.svg"
                className={styles['frame83']}
              />
            </div>
          </div>
          <div className={styles['frame71']}>
            <span className={styles['text24']}>
              <span>Login →</span>
            </span>
            <div className={styles['frame21']}>
              <span className={styles['text26']}>
                <span>Sign Up</span>
              </span>
            </div>
          </div>
        </div>
        <img
          alt="image62101"
          src="/image62101-7r2l-300h.png"
          className={styles['image6']}
        />
        <img
          alt="casuallife3dboysittingatthedeskwithopenbook92101"
          src="/casuallife3dboysittingatthedeskwithopenbook92101-7ygp-700h.png"
          className={styles['casuallife3dboysittingatthedeskwithopenbook9']}
        />
        <img
          alt="image122101"
          src="/image122101-xfsv-500w.png"
          className={styles['image12']}
        />
      </div>
    </div>
  )
}

export default Thumbnail
