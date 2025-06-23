# progress

## Metadata
- **Version**: 0.0.1
- **Description**: Visual representation of the status of a system process.
- **Category**: components

## Example Sections
1. **Linear progress indicators**
   - Description: 
2. **Circular progress indicators**
   - Description: 
3. **Custom progress indicators**
   - Description: 

## Examples
### Indeterminate linear progress indicator
- **Section**: Linear progress indicators
- **URL**: components/progress/indeterminate-progress
- **Tags**: docs
```tsx
import { VisaMediaPauseAltTiny, VisaMediaPlayAltTiny } from '@visa/nova-icons-react';
import { Button, ProgressLabel, ProgressLinear, Utility, UtilityFragment } from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'indeterminate-linear-progress';

export const IndeterminateProgress = () => {
  const [paused, setPaused] = useState(false);
  const [initiated, setInitiated] = useState(false);
  const [loadingMsg, setLoadingMsg] = useState('');

const start = () => {
  setInitiated(true);
  setTimeout(() => {
    setLoadingMsg('Loading...');
  }, 0);
}
  
const reset = () => {
  setInitiated(false);
  setLoadingMsg('');
}

  return (
    <Utility vFlexCol vGap={12}>
        {initiated && (
      <Utility vFlexGrow>
        <UtilityFragment vMarginVertical={8}>
          <ProgressLinear id={id} paused={paused} />
        </UtilityFragment>
        <ProgressLabel htmlFor={id}>
          <Utility tag="span" role="alert">{loadingMsg}</Utility>
        </ProgressLabel>
      </Utility>
        )}
      <Utility vMarginVertical={12} vFlex vGap={12}>
        <Button onClick={() => start()}>
          Start
        </Button>
        <Button colorScheme="secondary" onClick={() => reset()}>
          Reset
        </Button>
        <Button colorScheme="secondary" onClick={() => setPaused(!paused)}>
          {paused ? (
            <>
              <VisaMediaPlayAltTiny />
              Play
            </>
          ) : (
            <>
              <VisaMediaPauseAltTiny />
              Pause
            </>
          )}
        </Button>
      </Utility>
    </Utility>
  );
};

```

### Indeterminate linear progress indicator without visible label
- **Section**: Linear progress indicators
- **URL**: components/progress/indeterminate-no-label-progress
- **Tags**: docs
```tsx
import { VisaMediaPauseAltTiny, VisaMediaPlayAltTiny } from '@visa/nova-icons-react';
import { Button, ProgressLinear, Utility, UtilityFragment } from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'no-label-indeterminate-linear-progress';

export const IndeterminateNoLabelProgress = () => {
  const [paused, setPaused] = useState(false);
  const [initiated, setInitiated] = useState(false);
  const [loadingMsg, setLoadingMsg] = useState('');

const start = () => {
  setInitiated(true);
  setTimeout(() => {
    setLoadingMsg('Loading...');
  }, 500);
}
  
const reset = () => {
  setInitiated(false);
  setLoadingMsg('');
}

  return (
    <Utility vFlexCol vGap={12}>
      {initiated && (
      <Utility vFlexGrow>
        <UtilityFragment vMarginVertical={8}>
          <ProgressLinear aria-label="Please wait" id={id} paused={paused} />
        </UtilityFragment>
        <label className="v-progress-label v-sr" htmlFor={id}>
          <Utility tag="span" role="alert">{loadingMsg}</Utility>
        </label>
      </Utility>
      )}
    <Utility vMarginVertical={12} vFlex vGap={12}>
        <Button onClick={() => start()}>
          Start
        </Button>
        <Button colorScheme="secondary" onClick={() => reset()}>
          Reset
        </Button>
        <Button colorScheme="secondary" onClick={() => setPaused(!paused)}>
          {paused ? (
            <>
              <VisaMediaPlayAltTiny />
              Play
            </>
          ) : (
            <>
              <VisaMediaPauseAltTiny />
              Pause
            </>
          )}
        </Button>
      </Utility>
    </Utility>
  );
};

```

### Determinate linear progress indicator
- **Section**: Linear progress indicators
- **URL**: components/progress/determinate-progress
- **Tags**: docs
```tsx
import { Button, ProgressLabel, ProgressLinear, Utility, UtilityFragment } from '@visa/nova-react';
import { useCallback, useState, useRef } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'determinate-linear-progress';

export const DeterminateProgress = () => {
  const [value, setValue] = useState(0);
  const [loadingMsg, setLoadingMsg] = useState('');
  const countingRef = useRef(false);

  const startCountUp = useCallback(async () => {
    setValue(0);
    countingRef.current = true;
    setTimeout(() => setLoadingMsg('Loading...'), 500);
    for (let i = 0; i < 100; i++) {
      if (!countingRef.current) {
        resetCount();
        break;
      }
      await new Promise(resolve => setTimeout(resolve, 50)); // mock the time it takes to load
      setValue(prev => prev + 1); // increment the value by 1 percent
    }
    setLoadingMsg('Loading complete');
    countingRef.current = false;
  }, []);
  const resetCount = () => {
    countingRef.current = false;
    setValue(0);
    setLoadingMsg('');
  };
  return (
    <>
      <UtilityFragment vMarginVertical={8}>
        <ProgressLinear id={id} max={100} value={value}/>
      </UtilityFragment>
      <ProgressLabel htmlFor={id}>
        <span>Filename.jpg</span>
        <span>{value}%</span>
        <span role="alert" className='v-sr'>{loadingMsg}</span>
      </ProgressLabel>
      <Utility vMarginVertical={12} vFlex vGap={12}>
        <Button onClick={startCountUp}>
          Start
        </Button>
        <Button colorScheme="secondary" onClick={resetCount}>
          Reset
        </Button>
      </Utility>
    </>
  );
};

```

### Determinate linear progress indicator without visible label
- **Section**: Linear progress indicators
- **URL**: components/progress/determinate-no-label-progress
- **Tags**: docs
```tsx
import { Button, ProgressLabel, ProgressLinear, Utility, UtilityFragment } from '@visa/nova-react';
import { useCallback, useState, useRef } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'no-label-determinate-linear-progress';

export const DeterminateNoLabelProgress = () => {
  const [value, setValue] = useState(0);
  const [loadingMsg, setLoadingMsg] = useState('');
  const countingRef = useRef(false);

  const startCountUp = useCallback(async () => {
    setValue(0);
    countingRef.current = true;
    setTimeout(() => setLoadingMsg('Loading...'), 500);
    for (let i = 0; i < 100; i++) {
      if (!countingRef.current) {
        resetCount();
        break;
      }
      await new Promise(resolve => setTimeout(resolve, 50)); // mock the time it takes to load
      setValue(prev => prev + 1); // increment the value by 1 percent
    }
    setLoadingMsg('Loading complete');
    countingRef.current = false;
  }, []);
  const resetCount = () => {
    countingRef.current = false;
    setValue(0);
    setLoadingMsg('');
  };
  return (
    <>
      <UtilityFragment vMarginVertical={8}>
        <ProgressLinear id={id} max={100} value={value} />
      </UtilityFragment>
      <ProgressLabel htmlFor={id}>
        <span>{value}%</span>
        <span className="v-sr" role="alert">{loadingMsg}</span>
      </ProgressLabel>
      <Utility vMarginVertical={12} vFlex vGap={12}>
        <Button onClick={startCountUp}>
          Start
        </Button>
        <Button colorScheme="secondary" onClick={resetCount}>
          Reset
        </Button>
      </Utility>
    </>
  );
};

```

### Completed linear progress indicator
- **Section**: Linear progress indicators
- **URL**: components/progress/complete-progress
- **Tags**: docs
```tsx
import { VisaSuccessTiny } from '@visa/nova-icons-react';
import { ProgressLabel, ProgressLinear, Utility, UtilityFragment } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'complete-linear-progress';

export const CompleteProgress = () => {
  return (
    <>
      <UtilityFragment vMarginVertical={8}>
        <ProgressLinear completed id={id} max={100} value={100} aria-valuenow={100} />
      </UtilityFragment>
      <ProgressLabel htmlFor={id}>
        <Utility tag="span" vFlex vGap={4} role="alert">
          <VisaSuccessTiny />
          File is now uploaded.
        </Utility>
        <span>100%</span>
      </ProgressLabel>
    </>
  );
};

```

### Error linear progress indicator
- **Section**: Linear progress indicators
- **URL**: components/progress/error-progress
- **Tags**: docs
```tsx
import { ProgressLinear, ProgressLabel, UtilityFragment, Utility } from '@visa/nova-react';
import { VisaErrorTiny } from '@visa/nova-icons-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'error-determinate-linear-progress';

export const ErrorProgress = () => {
  return (
    <>
      <UtilityFragment vMarginVertical={8}>
        <ProgressLinear id={id} invalid max={100} value={0} />
      </UtilityFragment>
      <ProgressLabel htmlFor={id}>
        <Utility tag="span" vFlex vGap={4} role="alert">
          <VisaErrorTiny />
          This is required text that describes the error in more detail.
        </Utility>
        <span>0%</span>
      </ProgressLabel>
    </>
  );
};

```

### Small indeterminate circular progress indicator
- **Section**: Circular progress indicators
- **URL**: components/progress/indeterminate-circular-small-progress
- **Tags**: docs
```tsx
import { VisaMediaPauseAltTiny, VisaMediaPlayAltTiny } from '@visa/nova-icons-react';
import { Button, ProgressCircular, Utility } from '@visa/nova-react';
import { useState } from 'react';

export const IndeterminateCircularSmallProgress = () => {
  const [paused, setPaused] = useState(false);
  const [initiated, setInitiated] = useState(false);
  const [loadingMsg, setLoadingMsg] = useState('');

const start = () => {
  setInitiated(true);
  setTimeout(() => {
    setLoadingMsg('Loading...');
  }, 0);
}
  
const reset = () => {
  setInitiated(false);
  setLoadingMsg('');
}

  return (
    <Utility vFlexCol vGap={12}>
      {initiated && (
        <>
          <ProgressCircular
            className="v-flex-grow"
            indeterminate
            paused={paused}
            progressSize="small"
          />
          <span className="v-sr" role="alert">{loadingMsg}</span>
      </>
      )}
      <Utility vMarginVertical={12} vFlex vGap={12}>
        <Button onClick={() => start()}>
          Start
        </Button>
        <Button colorScheme="secondary" onClick={() => reset()}>
          Reset
        </Button>
        <Button colorScheme="secondary" onClick={() => setPaused(!paused)}>
          {paused ? (
            <>
              <VisaMediaPlayAltTiny />
              Play
            </>
          ) : (
            <>
              <VisaMediaPauseAltTiny />
              Pause
            </>
          )}
        </Button>
      </Utility>
    </Utility>
  );
};

```

### Large indeterminate circular progress indicator
- **Section**: Circular progress indicators
- **URL**: components/progress/indeterminate-circular-progress
- **Tags**: docs
```tsx
import { VisaMediaPauseAltTiny, VisaMediaPlayAltTiny } from '@visa/nova-icons-react';
import { Button, ProgressCircular, Utility } from '@visa/nova-react';
import { useState } from 'react';

export const IndeterminateCircularProgress = () => {
  const [paused, setPaused] = useState(false);
  const [initiated, setInitiated] = useState(false);
  const [loadingMsg, setLoadingMsg] = useState('');

const start = () => {
  setInitiated(true);
  setTimeout(() => {
    setLoadingMsg('Loading...');
  }, 0);
}
  
const reset = () => {
  setInitiated(false);
  setLoadingMsg('');
}

  return (
    <Utility vFlexCol vGap={12}>
      {initiated && (
      <ProgressCircular className="v-flex-grow" indeterminate paused={paused}>
        <span className="v-sr" role="alert">{loadingMsg}</span>
      </ProgressCircular>
      )}
      <Utility vMarginVertical={12} vFlex vGap={12}>
        <Button onClick={() => start()}>
          Start
        </Button>
        <Button colorScheme="secondary" onClick={() => reset()}>
          Reset
        </Button>
        <Button colorScheme="secondary" onClick={() => setPaused(!paused)}>
          {paused ? (
            <>
              <VisaMediaPlayAltTiny />
              Play
            </>
          ) : (
            <>
              <VisaMediaPauseAltTiny />
              Pause
            </>
          )}
        </Button>
      </Utility>
    </Utility>
  );
};

```

### Small determinate circular progress indicator
- **Section**: Circular progress indicators
- **URL**: components/progress/determinate-circular-small-progress
- **Tags**: docs
```tsx
import { Button, ProgressCircular, Typography, Utility } from '@visa/nova-react';
import { useCallback, useState, useRef } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'small-determinate-circular-progress';

export const DeterminateCircularSmallProgress = () => {
  const [value, setValue] = useState(0);
  const countingRef = useRef(false);
  const [loadingMsg, setLoadingMsg] = useState('');
  

  const startCountUp = useCallback(async () => {
    setValue(0);
    countingRef.current = true;
    setLoadingMsg('Loading...');
    for (let i = 0; i < 100; i++) {
      if (!countingRef.current) {
        resetCount();
        break;
      }
      await new Promise(resolve => setTimeout(resolve, 50)); // mock the time it takes to load
      setValue(prev => prev + 1); // increment the value by 1 percent
    }
    setLoadingMsg('Loading complete');
    countingRef.current = false;
  }, []);
  const resetCount = () => {
    countingRef.current = false;
    setValue(0);
    setLoadingMsg('');
  };
  return (
    <>
      <ProgressCircular aria-labelledby={id} progressSize="small" value={value} aria-valuenow={value}>
        <Typography tag="div" className="v-progress-label" variant="body-2-bold" id={id}>{value}%</Typography>
      </ProgressCircular>
      <Utility tag="span" role="alert" className="v-sr">{loadingMsg}</Utility>
      <Utility vMarginVertical={12} vFlex vGap={12}>
        <Button onClick={startCountUp}>
          Start
        </Button>
        <Button colorScheme="secondary" onClick={resetCount}>
          Reset
        </Button>
      </Utility>
    </>
  );
};

```

### Large determinate circular progress indicator
- **Section**: Circular progress indicators
- **URL**: components/progress/determinate-circular-progress
- **Tags**: docs
```tsx
import { Button, ProgressCircular, ProgressLabel, Typography, Utility } from '@visa/nova-react';
import { useCallback, useState, useRef } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'large-determinate-circular-progress';

export const DeterminateCircularProgress = () => {
  const [value, setValue] = useState(0);
  const countingRef = useRef(false);
  const [loadingMsg, setLoadingMsg] = useState('');
  const startCountUp = useCallback(async () => {
    setValue(0);
    countingRef.current = true;
    setLoadingMsg('Loading...');
    for (let i = 0; i < 100; i++) {
      if (!countingRef.current) {
        resetCount();
        break;
      }
      await new Promise(resolve => setTimeout(resolve, 50)); // mock the time it takes to load
      setValue(prev => prev + 1); // increment the value by 1 percent
    }
    setLoadingMsg('Loading complete');
    countingRef.current = false;
  }, []);
  const resetCount = () => {
    countingRef.current = false;
    setValue(0);
    setLoadingMsg('');
  };
  return (
    <>
      <ProgressCircular aria-labelledby={id} value={value} aria-valuenow={value}>
        <ProgressLabel id={id}>
          <Typography tag="div" className="v-progress-label" variant="body-2-bold">{value}%</Typography>
        </ProgressLabel>
      </ProgressCircular>
      <Utility tag="span" role="alert" className="v-sr">{loadingMsg}</Utility>
      <Utility vMarginVertical={12} vFlex vGap={12}>
        <Button onClick={startCountUp}>
          Start
        </Button>
        <Button colorScheme="secondary" onClick={resetCount}>
          Reset
        </Button>
      </Utility>
    </>
  );
};

```

### Completed determinate circular progress indicator
- **Section**: Circular progress indicators
- **URL**: components/progress/complete-circular-progress
- **Tags**: docs
```tsx
import { ProgressCircular, Typography, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'large-complete-circular-progress';
const value = 100;

export const CompleteCircularProgress = () => {
  return (
    <>
      <ProgressCircular aria-labelledby={`${id} completed-circular-screen-reader-message`} value={value} aria-valuenow={value}>
        <Typography id={id} tag="div" className="v-progress-label" variant="body-2-bold">{value}%</Typography>
      </ProgressCircular>
      <Utility tag="span" role="alert" className="v-sr" id="completed-circular-screen-reader-message">Loading complete.</Utility>
    </>
  );
};

```

### Error determinate circular progress indicator
- **Section**: Circular progress indicators
- **URL**: components/progress/error-circular-progress
- **Tags**: docs
```tsx
import { VisaErrorTiny } from '@visa/nova-icons-react';
import { InputMessage } from '@visa/nova-react';

export const ErrorCircularProgress = () => {
  return (
    <InputMessage className='v-input-error' role="alert">
      <VisaErrorTiny />
      This is required text that describes the error in more detail.
    </InputMessage>
  );
};

```

### Custom size determinate circular progress indicator
- **Section**: Custom progress indicators
- **URL**: components/progress/circular-custom-size-progress
- **Tags**: custom
```tsx
import { Button, ProgressCircular, ProgressLabel, Typography, Utility } from '@visa/nova-react';
import { useCallback, useState, useRef } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'circular-custom-size-determinate-progress';

export const CircularCustomSizeProgress = () => {
  const [value, setValue] = useState(0);
  const countingRef = useRef(false);
  const [loadingMsg, setLoadingMsg] = useState('');
  const startCountUp = useCallback(async () => {
    setValue(0);
    countingRef.current = true;
    setLoadingMsg('Loading...');
    for (let i = 0; i < 100; i++) {
      if (!countingRef.current) {
        resetCount();
        break;
      }
      await new Promise(resolve => setTimeout(resolve, 50)); // mock the time it takes to load
      setValue(prev => prev + 1); // increment the value by 1 percent
    }
    setLoadingMsg('Loading complete');
    countingRef.current = false;
  }, []);
  const resetCount = () => {
    countingRef.current = false;
    setValue(0);
    setLoadingMsg('');
  };
  return (
    <>
      <ProgressCircular aria-labelledby={id} progressSize={100} value={value} aria-valuenow={value}>
        <ProgressLabel id={id}>
          <Typography tag="div" className="v-progress-label" variant="body-2-bold">
            {value}%
          </Typography>
        </ProgressLabel>
      </ProgressCircular>
      <Utility tag="span" role="alert" className="v-sr">{loadingMsg}</Utility>
      <Utility vMarginVertical={12} vFlex vGap={12}>
        <Button onClick={startCountUp}>
          Start
        </Button>
        <Button colorScheme="secondary" onClick={resetCount}>
          Reset
        </Button>
      </Utility>
    </>
  );
};

```

## Property Sections
### Progress
- **Selector**: <Progress />
- **Description**: Visual representation of the status of a system process.

### ProgressCircular
- **Selector**: <ProgressCircular />
- **Description**: Circular indicator used to show the progress of a task or process.

### ProgressLabel
- **Selector**: <ProgressLabel />
- **Description**: Label used with a progress component for textual representation of status.

### ProgressLinear
- **Selector**: <ProgressLinear />
- **Description**: Linear indicator used to show the progress of a task or process.

## Properties
### completed
- **Section**: Progress
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Is Completed

### indeterminate
- **Section**: Progress
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: If the Progress is Indeterminate Progress

### invalid
- **Section**: Progress
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Is Error State

### paused
- **Section**: Progress
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Is Paused

### progressSize
- **Section**: Progress
- **Type**: number , "small" , "large"
- **Default**: large
- **Required**: false
- **Description**: Width of the Circular Progress

### progressType
- **Section**: Progress
- **Type**: "circular" , "linear"
- **Default**: linear
- **Required**: false
- **Description**: 

### ref
- **Section**: Progress
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Progress
- **Type**: ElementType
- **Default**: 
- **Required**: false
- **Description**: Tag of Component

### indeterminate
- **Section**: ProgressCircular
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: If the Progress is Indeterminate Progress

### paused
- **Section**: ProgressCircular
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Is Paused

### progressSize
- **Section**: ProgressCircular
- **Type**: number , "small" , "large"
- **Default**: large
- **Required**: false
- **Description**: Width of the Circular Progress

### ref
- **Section**: ProgressCircular
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### ref
- **Section**: ProgressLabel
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: ProgressLabel
- **Type**: ElementType
- **Default**: label
- **Required**: false
- **Description**: Tag of Component

### completed
- **Section**: ProgressLinear
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Is Completed

### invalid
- **Section**: ProgressLinear
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Is Error State

### paused
- **Section**: ProgressLinear
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Is Paused

### ref
- **Section**: ProgressLinear
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: ProgressLinear
- **Type**: ElementType
- **Default**: progress
- **Required**: false
- **Description**: Tag of Component

