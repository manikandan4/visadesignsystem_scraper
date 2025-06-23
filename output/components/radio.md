# radio

## Metadata
- **Version**: 0.0.1
- **Description**: Interactive elements that allow users to select a single option from a list.
- **Category**: components

## Example Sections
1. **Default radio buttons**
   - Description: 
2. **Radio button groups**
   - Description: 
3. **Radio button panels**
   - Description: 
4. **Radio button panel groups**
   - Description: 

## Examples
### Radio button with label
- **Section**: Default radio buttons
- **URL**: components/radio/with-label-radio
- **Tags**: 
```tsx
import { Label, Radio, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-radio';

export const DefaultRadio = () => {
  return (
    <Utility vAlignItems="center" vFlex vGap={2}>
      <Radio id={id} name={id} />
      <Label htmlFor={id}>Label</Label>
    </Utility>
  );
};

```

### Radio button without visible label
- **Section**: Default radio buttons
- **URL**: components/radio/without-visible-label-radio
- **Tags**: 
```tsx
import { Radio, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'no-label-radio';

export const NoLabelRadio = () => {
  return (
    <Utility vAlignItems="center" vFlex vGap={2}>
      <Radio id={id} aria-label="Label" name={id} />
    </Utility>
  );
};

```

### Radio button with description
- **Section**: Default radio buttons
- **URL**: components/radio/with-description-radio
- **Tags**: 
```tsx
import { InputMessage, Label, Radio, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'with-description-radio';

export const WithDescriptionRadio = () => {
  return (
    <fieldset aria-labelledby={`${id}-message`}>
      <Utility vFlex vGap={2}>
        <Radio id={id} name={id} />
        <Utility vFlex vFlexCol vGap={2} vMarginVertical={10}>
          <Label htmlFor={id}>Label</Label>
          <InputMessage id={`${id}-message`}>
            This is optional text that describes the label in more detail.
          </InputMessage>
        </Utility>
      </Utility>
    </fieldset>
  );
};

```

### Selected radio button
- **Section**: Default radio buttons
- **URL**: components/radio/selected-radio
- **Tags**: 
```tsx
import { Label, Radio, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'selected-radio';

export const SelectedRadio = () => {
  return (
    <Utility vAlignItems="center" vFlex vGap={2}>
      <Radio defaultChecked id={id} name={id} />
      <Label htmlFor={id}>Label</Label>
    </Utility>
  );
};

```

### Radio button with error
- **Section**: Default radio buttons
- **URL**: components/radio/error-radio
- **Tags**: 
```tsx
import { ChangeEvent, useRef, useState } from 'react';
import { VisaErrorTiny } from '@visa/nova-icons-react';
import { Button, InputMessage, Label, Radio, Utility, UtilityFragment } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'radio-error';

export const ErrorRadio = () => {
  const radioRef = useRef<HTMLInputElement>(null);
  const [checked, setChecked] = useState(false);
  const [invalid, setInvalid] = useState(false);

  const onRadioButtonChange = (event: ChangeEvent<HTMLInputElement>) => {
    setChecked(event.target.checked);
  };

  const onSubmit = () => {
    if (checked) setInvalid(false);
    else {
      setInvalid(true);
      radioRef.current?.focus();
    }
  };
  return (
    <>
      <fieldset aria-labelledby={`${id}-message`}>
        <Utility vFlex vAlignItems="center" vGap={2}>
          <Radio
            aria-invalid={invalid}
            aria-required="true"
            checked={checked}
            id={id}
            name={id}
            onChange={onRadioButtonChange}
            ref={radioRef}
          />
          <Label htmlFor={id} id={`${id}-label`}>
            Label
          </Label>
        </Utility>
        {invalid && (
          <UtilityFragment vAlignItems="center" vFlex vGap={2} vMarginTop={4}>
            <InputMessage
              aria-atomic="true"
              aria-live="assertive"
              className="v-typography-label"
              id={`${id}-message`}
              role="alert"
            >
              <VisaErrorTiny />
              This is required text that describes the error in more detail.
            </InputMessage>
          </UtilityFragment>
        )}
      </fieldset>
      <Utility vFlex vGap={12} vMarginTop={12}>
        <Button onClick={onSubmit}>Submit</Button>
        <Button colorScheme="secondary" onClick={() => setChecked(false)}>
          Reset
        </Button>
      </Utility>
    </>
  );
};

```

### Disabled radio button
- **Section**: Default radio buttons
- **URL**: components/radio/disabled-radio
- **Tags**: 
```tsx
import { Label, Radio, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'radio-disabled';

export const DisabledRadio = () => {
  return (
    <Utility vAlignItems="center" vFlex vGap={2}>
      <Radio disabled id={id} name={id} />
      <Label htmlFor={id}>Label</Label>
    </Utility>
  );
};

```

### Disabled and selected radio button
- **Section**: Default radio buttons
- **URL**: components/radio/disabled-selected-radio
- **Tags**: 
```tsx
import { Label, Radio, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'radio-disabled-selected';

export const DisabledSelectedRadio = () => {
  return (
    <Utility vAlignItems="center" vFlex vGap={2}>
      <Radio defaultChecked disabled id={id} name={id} />
      <Label htmlFor={id}>Label</Label>
    </Utility>
  );
};

```

### Radio button group
- **Section**: Radio button groups
- **URL**: components/radio/group-radio
- **Tags**: 
```tsx
import { Label, Radio, Typography, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'group-radio';

const radios = ['Label 1', 'Label 2', 'Label 3'];

export const GroupRadio = () => {
  return (
    <fieldset>
      <Typography tag="legend" variant="label">
        Group label (required)
      </Typography>
      <Utility vFlex vFlexCol vGap={4}>
        {radios.map((radio, index) => (
          <Utility key={`${id}-option-${index}`} vAlignItems="center" vFlex vGap={2}>
            <Radio id={`${id}-option-${index}`} name={`${id}-options`} />
            <Label htmlFor={`${id}-option-${index}`}>{radio}</Label>
          </Utility>
        ))}
      </Utility>
    </fieldset>
  );
};

```

### Radio button group with error
- **Section**: Radio button groups
- **URL**: components/radio/error-group-radio
- **Tags**: 
```tsx
import { VisaErrorTiny } from '@visa/nova-icons-react';
import { ChangeEvent, useRef, useState } from 'react';
import { Button, InputMessage, Label, Radio, Typography, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'error-group-radio';

const radios = ['Label 1', 'Label 2', 'Label 3'];

export const ErrorGroupRadio = () => {
  const ref = useRef<HTMLInputElement>(null);
  const [errorState, setErrorState] = useState(false);
  const [option, setOption] = useState('');

  const handleChangeState = (e: ChangeEvent<HTMLInputElement>) => {
    setOption(e.target.value);
  };
  const handleOnSubmit = () => {
    if (option !== '') {
      setErrorState(false);
    } else {
      setOption('');
      setErrorState(true);
    }
    ref?.current?.focus();
  };

  return (
    <>
      <fieldset aria-invalid={errorState} aria-labelledby={`${id}-legend ${id}-message`}>
        <Typography id={`${id}-legend`} tag="legend" variant="label">
          Group label (required)
        </Typography>
        <Utility vFlex vFlexCol vGap={4}>
          {radios.map((radio, index) => (
            <Utility key={`${id}-option-${index}`} vAlignItems="center" vFlex vGap={2}>
              <Radio
                aria-invalid={errorState}
                checked={option === index.toString()}
                id={`${id}-option-${index}`}
                name={`${id}-options`}
                onChange={handleChangeState}
                ref={index === 0 ? ref : undefined}
                value={index}
              />
              <Label htmlFor={`${id}-option-${index}`}>{radio}</Label>
            </Utility>
          ))}
        </Utility>
        {errorState && (
          <InputMessage
            aria-atomic="true"
            aria-live="assertive"
            className="v-typography-label v-flex v-align-items-center"
            id={`${id}-message`}
            role="alert"
          >
            <VisaErrorTiny />
            This is required text that describes the error in more detail.
          </InputMessage>
        )}
      </fieldset>
      <Utility vFlex vFlexRow vPaddingTop={4} vGap={12}>
        <Button onClick={handleOnSubmit}>Submit</Button>
        <Button colorScheme="secondary" onClick={() => setOption('')}>
          Reset
        </Button>
      </Utility>
    </>
  );
};

```

### Horizontal radio button group
- **Section**: Radio button groups
- **URL**: components/radio/horizontal-group-radio
- **Tags**: 
```tsx
import { Label, Radio, Typography, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'horizontal-group-radio';

const radios = ['Label 1', 'Label 2', 'Label 3'];

export const HorizontalGroupRadio = () => {
  return (
    <fieldset>
      <Typography tag="legend" variant="label">
        Group label (required)
      </Typography>
      <Utility vFlex vFlexRow vGap={24} vFlexWrap>
        {radios.map((radio, index) => (
          <Utility key={`${id}-option-${index}`} vFlex vAlignItems="center" vGap={2}>
            <Radio id={`${id}-option-${index}`} name={`${id}-options`} />
            <Label htmlFor={`${id}-option-${index}`}>{radio}</Label>
          </Utility>
        ))}
      </Utility>
    </fieldset>
  );
};

```

### Radio button panel
- **Section**: Radio button panels
- **URL**: components/radio/with-description-panel-radio
- **Tags**: 
```tsx
import { InputMessage, Radio, RadioPanel, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'with-description-panel-radio';

export const WithDescriptionPanelRadio = () => {
  return (
    <fieldset aria-labelledby={`${id}-message`}>
      <RadioPanel className="v-align-items-start" htmlFor={id}>
        <Utility vFlex vGap={2} style={{ inlineSize: '100%' }}>
          <Radio className="v-flex-shrink-0" id={id} name={id} />
          <Utility vFlex vFlexCol vGap={2} vMarginVertical={8}>
            Label
            <InputMessage id={`${id}-message`}>
              This is optional text that describes the label in more detail.
            </InputMessage>
          </Utility>
        </Utility>
      </RadioPanel>
    </fieldset>
  );
};

```

### Radio button panel without description
- **Section**: Radio button panels
- **URL**: components/radio/without-description-panel-radio
- **Tags**: 
```tsx
import { Radio, RadioPanel, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'with-description-panel-radio';

export const WithoutDescriptionPanelRadio = () => {
  return (
    <RadioPanel className="v-align-items-start" htmlFor={id}>
      <Utility vAlignItems="center" vFlex vGap={2} style={{ inlineSize: '100%' }}>
        <Radio className="v-flex-shrink-0" id={id} name={id} />
        Label
      </Utility>
    </RadioPanel>
  );
};

```

### Disabled radio button panel
- **Section**: Radio button panels
- **URL**: components/radio/disabled-panel-radio
- **Tags**: 
```tsx
import { InputMessage, Radio, RadioPanel, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'radio-panel-disabled';

export const DisabledPanelRadio = () => {
  return (
    <fieldset aria-labelledby={`${id}-message`}>
      <RadioPanel className="v-align-items-start" htmlFor={id}>
        <Utility vFlex vGap={2} style={{ inlineSize: '100%' }}>
          <Radio className="v-flex-shrink-0" disabled id={id} name="radio-13" />
          <Utility vFlex vFlexCol vGap={2} vMarginVertical={8}>
            Label
            <InputMessage id={`${id}-message`}>
              This is optional text that describes the label in more detail.
            </InputMessage>
          </Utility>
        </Utility>
      </RadioPanel>
    </fieldset>
  );
};

```

### Radio button panel group
- **Section**: Radio button panel groups
- **URL**: components/radio/group-panel-radio
- **Tags**: 
```tsx
import { InputMessage, Radio, RadioPanel, Typography, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'group-panel-radio';

const radios = ['Label 1', 'Label 2', 'Label 3'];

export const GroupPanelRadio = () => {
  return (
    <fieldset aria-labelledby={`${id}-legend`}>
      <Typography id={`${id}-legend`} tag="legend" variant="label">
        Group label (required)
      </Typography>
      <Utility vFlex vFlexCol vGap={8}>
        {radios.map((radio, index) => (
          <RadioPanel className="v-align-items-start" htmlFor={`${id}-option-${index}`} key={`${id}-option-${index}`}>
            <Utility vFlex vGap={2} style={{ inlineSize: '100%' }}>
              <Radio className="v-flex-shrink-0" id={`${id}-option-${index}`} name={`${id}-options`} />
              <Utility vFlex vFlexCol vGap={2} vMarginVertical={8}>
                {radio}
                <InputMessage id={`${id}-radio-${index}-message`}>
                  This is optional text that describes the label in more detail.
                </InputMessage>
              </Utility>
            </Utility>
          </RadioPanel>
        ))}
      </Utility>
    </fieldset>
  );
};

```

### Radio button panel group with error
- **Section**: Radio button panel groups
- **URL**: components/radio/error-group-panel-radio
- **Tags**: 
```tsx
import { VisaErrorTiny } from '@visa/nova-icons-react';
import { Utility, RadioPanel, Radio, Label, InputMessage, Button, Typography } from '@visa/nova-react';
import { ChangeEvent, useRef, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'error-group-panel-radio';

const radios = ['Label 1', 'Label 2', 'Label 3'];

export const ErrorPanelGroupRadio = () => {
  const ref = useRef<HTMLInputElement>(null);
  const [errorState, setErrorState] = useState(false);
  const [option, setOption] = useState('');

  const handleChangeState = (e: ChangeEvent<HTMLInputElement>) => {
    setOption(e.target.value);
  };
  const handleOnSubmit = () => {
    if (option !== '') {
      setErrorState(false);
    } else {
      setOption('');
      setErrorState(true);
    }
    ref?.current?.focus();
  };
  return (
    <>
      <fieldset aria-labelledby={`${id}-legend ${id}-message`}>
        <Typography id={`${id}-legend`} tag="legend" variant="label">
          Group label (required)
        </Typography>
        <Utility vFlex vFlexCol vGap={8}>
          {radios.map((radio, index) => (
            <RadioPanel className="v-align-items-start" htmlFor={`${id}-option-${index}`} key={`${id}-option-${index}`}>
              <Utility vFlex vGap={2} style={{ inlineSize: '100%' }}>
                <Radio
                  aria-describedby={`${id}-option-${index}-message`}
                  aria-invalid={errorState}
                  checked={option === `${index}`}
                  className="v-flex-shrink-0"
                  id={`${id}-option-${index}`}
                  name={`${id}-options`}
                  onChange={handleChangeState}
                  ref={index === 0 ? ref : undefined}
                  value={index}
                />
                <Utility vFlex vFlexCol vGap={2} vMarginVertical={8}>
                  <Label htmlFor={`${id}-option-${index}`}>{radio}</Label>
                  <InputMessage id={`${id}-option-${index}-message`}>
                    This is optional text that describes the label in more detail.
                  </InputMessage>
                </Utility>
              </Utility>
            </RadioPanel>
          ))}
        </Utility>
        {errorState && (
          <InputMessage
            aria-atomic="true"
            aria-live="assertive"
            className="v-typography-label v-flex v-align-items-center"
            id={`${id}-message`}
            role="alert"
          >
            <VisaErrorTiny />
            This is required text that describes the error in more detail.
          </InputMessage>
        )}
      </fieldset>
      <Utility vFlex vFlexRow vPaddingTop={12} vGap={12}>
        <Button onClick={handleOnSubmit}>Submit</Button>
        <Button colorScheme="secondary" onClick={() => setOption('')}>
          Reset
        </Button>
      </Utility>
    </>
  );
};

```

## Property Sections
### Radio
- **Selector**: <Radio />
- **Description**: Interactive elements that allow users to select a single option from a list.

### RadioPanel
- **Selector**: <RadioPanel />
- **Description**: Container used with a radio component to add a border and background color.

## Properties
### ref
- **Section**: Radio
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Radio
- **Type**: ElementType
- **Default**: input
- **Required**: false
- **Description**: Tag of Component

### ref
- **Section**: RadioPanel
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: RadioPanel
- **Type**: ElementType
- **Default**: 
- **Required**: false
- **Description**: Tag of Component

