# input

## Metadata
- **Version**: 0.0.1
- **Description**: Text fields that enable users to enter free-form content.
- **Category**: components

## Example Sections
1. **Single-line inputs**
   - Description: 
2. **Multi-line inputs**
   - Description: 
3. **Custom inputs**
   - Description: 

## Examples
### Default input
- **Section**: Single-line inputs
- **URL**: components/input/default-input
- **Tags**: docs
```tsx
import { Input, InputContainer, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'input-default';

export const DefaultInput = () => {
  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Input aria-required="true" id={id} type="text" />
      </InputContainer>
    </Utility>
  );
};

```

### Input with initial value
- **Section**: Single-line inputs
- **URL**: components/input/initial-value-input
- **Tags**: docs
```tsx
import { Input, InputContainer, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'input-initial-value';

export const InitialValueInput = () => {
  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Input aria-required="true" defaultValue="Initial value" id={id} type="text" />
      </InputContainer>
    </Utility>
  );
};

```

### Input with inline message
- **Section**: Single-line inputs
- **URL**: components/input/inline-message-input
- **Tags**: docs
```tsx
import { Input, InputContainer, InputMessage, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'input-inline-message';

export const InlineMessageInput = () => {
  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Input aria-describedby={`${id}-message`} aria-required="true" id={id} type="text" />
      </InputContainer>
      <InputMessage id={`${id}-message`}>This is optional text that describes the label in more detail.</InputMessage>
    </Utility>
  );
};

```

### Input with clear text button
- **Section**: Single-line inputs
- **URL**: components/input/clear-button-input
- **Tags**: docs
```tsx
import { VisaClearAltTiny } from '@visa/nova-icons-react';
import { Button, Input, InputContainer, Label, Utility } from '@visa/nova-react';
import { FocusEvent, useEffect, useRef, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'input-clear-button';

export const ClearButtonInput = () => {
  const [showClearButton, setShowClearButton] = useState(false);
  const [inputValue, setInputValue] = useState('');

  const inputRef = useRef<HTMLInputElement>(null);

  const handleBlur = (event: FocusEvent<HTMLDivElement>) => {
    if (!event.currentTarget.contains(event.relatedTarget)) {
      setShowClearButton(false);
    }
  };

  const handleClear = () => {
    setInputValue('');
    // Put focus back into the input
    if (inputRef.current) {
      inputRef.current.focus();
    }
  };

  useEffect(() => {
    if (inputValue !== '') setShowClearButton(true);
    else setShowClearButton(false);
  }, [inputValue]);

  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer
        onBlur={e => handleBlur(e)}
        onFocus={() => {
          if (inputValue !== '') setShowClearButton(true);
        }}
      >
        <Input
          ref={inputRef}
          aria-required="true"
          id={id}
          onChange={e => setInputValue(e.currentTarget.value)}
          type="text"
          value={inputValue}
        />
        {showClearButton && (
          <Button aria-label="Clear" buttonSize="small" colorScheme="tertiary" iconButton onClick={handleClear} subtle>
            <VisaClearAltTiny />
          </Button>
        )}
      </InputContainer>
    </Utility>
  );
};

```

### Read-only input
- **Section**: Single-line inputs
- **URL**: components/input/read-only-input
- **Tags**: docs
```tsx
import { Checkbox, Input, InputContainer, Label, Utility } from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'input-readonly';

export const ReadOnlyInput = () => {
  const [readonly, setReadonly] = useState(true);

  return (
    <>
      <Utility vFlex vFlexCol vGap={4}>
        <Label htmlFor={id}>Label (required)</Label>
        <InputContainer>
          <Input aria-required="true" defaultValue="Read-only example text." id={id} readOnly={readonly} type="text" />
        </InputContainer>
      </Utility>
      <Utility vAlignItems="center" vFlex vGap={2} vMarginTop={24}>
        <Checkbox checked={readonly} id={`${id}-checkbox`} onChange={() => setReadonly(!readonly)} />
        <Label htmlFor={`${id}-checkbox`}>Mark input as read-only</Label>
      </Utility>
    </>
  );
};

```

### Disabled input
- **Section**: Single-line inputs
- **URL**: components/input/disabled-input
- **Tags**: docs
```tsx
import { Checkbox, Input, InputContainer, Label, Utility } from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'disabled-input';

export const DisabledInput = () => {
  const [disabled, setDisabled] = useState(true);

  return (
    <>
      <Utility vFlex vFlexCol vGap={4}>
        <Label htmlFor={id}>Label (required)</Label>
        <InputContainer>
          <Input aria-required="true" disabled={disabled} id={id} type="text" />
        </InputContainer>
      </Utility>
      <Utility vAlignItems="center" vFlex vGap={2} vMarginTop={24}>
        <Checkbox checked={disabled} id={`${id}-checkbox`} onChange={() => setDisabled(!disabled)} />
        <Label htmlFor={`${id}-checkbox`}>Mark input as disabled</Label>
      </Utility>
    </>
  );
};

```

### Input with error
- **Section**: Single-line inputs
- **URL**: components/input/error-input
- **Tags**: docs
```tsx
import { VisaErrorTiny } from '@visa/nova-icons-react';
import { ChangeEvent, useRef, useState } from 'react';
import { Button, Input, InputContainer, InputMessage, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'input-error';

const DEFAULT_INPUT_STATE = {
  value: '',
  error: false,
};

export const ErrorInput = () => {
  const [inputState, setInputState] = useState(DEFAULT_INPUT_STATE);

  const inputRef = useRef<HTMLInputElement>(null);

  const handleSubmit = () => {
    // Customize this for your own validation needs
    setInputState(prevInputState => ({
      ...prevInputState,
      error: true,
    }));

    // Focus on the input with error
    if (inputRef.current) {
      inputRef.current.focus();
    }
  };

  const handleReset = () => {
    setInputState(DEFAULT_INPUT_STATE);
  };
  const handleInputChange = (e: ChangeEvent<HTMLInputElement>) => {
    setInputState({
      value: e.target.value,
      error: false,
    });
  };

  return (
    <>
      <Utility vFlex vFlexCol vGap={4}>
        <Label htmlFor={id}>Label (required)</Label>
        <InputContainer>
          <Input
            aria-describedby={`${id}-message`}
            aria-invalid={inputState.error}
            aria-required="true"
            ref={inputRef}
            id={id}
            type="text"
            value={inputState.value}
            onChange={handleInputChange}
          />
        </InputContainer>
        {inputState.error && (
          <InputMessage aria-atomic="true" aria-live="assertive" id={`${id}-message`} role="alert">
            <VisaErrorTiny />
            This is required text that describes the error in more detail.
          </InputMessage>
        )}
      </Utility>
      <Utility vFlex vGap={12} vMarginTop={16}>
        <Button id={`${id}-submit-button`} onClick={handleSubmit}>
          Submit
        </Button>
        <Button id={`${id}-reset-button`} colorScheme="secondary" onClick={handleReset}>
          Reset
        </Button>
      </Utility>
    </>
  );
};

```

### Input with prefix
- **Section**: Single-line inputs
- **URL**: components/input/prefix-input
- **Tags**: docs
```tsx
import { Input, InputContainer, Label, Typography, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'input-prefix';

export const PrefixInput = () => {
  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Typography id={`${id}-prefix`} tag="span" variant="body-2-bold">
          $
        </Typography>
        <Input aria-describedby={`${id}-prefix`} aria-required="true" id={id} type="text" />
      </InputContainer>
    </Utility>
  );
};

```

### Input with suffix
- **Section**: Single-line inputs
- **URL**: components/input/suffix-input
- **Tags**: docs
```tsx
import { Input, InputContainer, Label, Typography, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'input-suffix';

export const SuffixInput = () => {
  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Input aria-describedby={`${id}-suffix`} aria-required="true" id={id} type="text" />
        <Typography id={`${id}-suffix`} tag="span" variant="body-2-bold">
          %
        </Typography>
      </InputContainer>
    </Utility>
  );
};

```

### Input with action button
- **Section**: Single-line inputs
- **URL**: components/input/action-button-input
- **Tags**: docs
```tsx
import { VisaPasswordHideTiny, VisaPasswordShowTiny } from '@visa/nova-icons-react';
import { Button, Input, InputContainer, Label, Utility } from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'input-action-button';

export const ActionButtonInput = () => {
  const [showPassword, setShowPassword] = useState(true);

  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Input aria-required="true" id={id} type={showPassword ? 'text' : 'password'} />
        <Button
          aria-label={showPassword ? 'hide text' : 'show text'}
          buttonSize="small"
          colorScheme="tertiary"
          iconButton
          onClick={() => setShowPassword(!showPassword)}
        >
          {showPassword ? <VisaPasswordHideTiny /> : <VisaPasswordShowTiny />}
        </Button>
      </InputContainer>
    </Utility>
  );
};

```

### Input with masked field
- **Section**: Single-line inputs
- **URL**: components/input/mask-button-input
- **Tags**: docs
```tsx
import { VisaPasswordHideTiny, VisaPasswordShowTiny } from '@visa/nova-icons-react';
import { Button, Input, InputContainer, Label, Utility } from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'input-mask-button';

export const MaskButtonInput = () => {
  const [showPassword, setShowPassword] = useState(false);

  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Input aria-required="true" defaultValue="password" id={id} type={showPassword ? 'text' : 'password'} />
        <Button
          aria-label={showPassword ? 'hide text' : 'show text'}
          buttonSize="small"
          colorScheme="tertiary"
          iconButton
          onClick={() => setShowPassword(!showPassword)}
        >
          {showPassword ? <VisaPasswordHideTiny /> : <VisaPasswordShowTiny />}
        </Button>
      </InputContainer>
    </Utility>
  );
};

```

### Input with leading icon
- **Section**: Single-line inputs
- **URL**: components/input/leading-icon-input
- **Tags**: docs
```tsx
import { VisaAccountLow } from '@visa/nova-icons-react';
import { Input, InputContainer, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'input-leading-icon';

export const LeadingIconInput = () => {
  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Utility vFlex vFlexCol>
          <VisaAccountLow />
        </Utility>
        <Input aria-required="true" id={id} type="text" />
      </InputContainer>
    </Utility>
  );
};

```

### One-time passcode input
- **Section**: Single-line inputs
- **URL**: components/input/one-time-passcode-input
- **Tags**: docs
```tsx
import { Input, InputContainer, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'input-otp';

export const OneTimePasscodeInput = () => {
  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label</Label>
      <InputContainer style={{ inlineSize: '160px' }}>
        <Input aria-required="true" id={id} otp type="text" />
      </InputContainer>
    </Utility>
  );
};

```

### Native textarea with resize property
- **Section**: Multi-line inputs
- **URL**: components/input/native-resize-textarea
- **Tags**: 
```tsx
import { InputContainer, Label, Textarea, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'native-text-area-resize';

export const NativeResizeTextarea = () => {
  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer className="v-flex-row">
        <Textarea aria-required="true" id={id} name={id} />
      </InputContainer>
    </Utility>
  );
};

```

### Native textarea without resize property
- **Section**: Multi-line inputs
- **URL**: components/input/native-no-resize-textarea
- **Tags**: 
```tsx
import { InputContainer, Label, Textarea, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'text-area-no-resize';

export const NativeNoResizeTextarea = () => {
  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer className="v-flex-row">
        <Textarea aria-required="true" fixed id={id} name={id} />
      </InputContainer>
    </Utility>
  );
};

```

### Textarea with fixed height
- **Section**: Multi-line inputs
- **URL**: components/input/fixed-height-textarea
- **Tags**: docs
```tsx
import { InputContainer, Label, Textarea, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'text-area-fixed-height';

export const FixedHeightTextarea = () => {
  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer className="v-flex-row">
        <Textarea aria-required="true" fixed id={id} name={id} style={{ blockSize: '130px' }} />
      </InputContainer>
    </Utility>
  );
};

```

### Textarea with fixed height and resize property
- **Section**: Multi-line inputs
- **URL**: components/input/resize-textarea
- **Tags**: docs
```tsx
import { InputContainer, Label, Textarea, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'text-area-resize-height';

export const ResizeTextarea = () => {
  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer className="v-flex-row">
        <Textarea aria-required="true" id={id} name={id} style={{ blockSize: '130px' }} />
      </InputContainer>
    </Utility>
  );
};

```

### Textarea with fixed height and character counter
- **Section**: Multi-line inputs
- **URL**: components/input/text-count-textarea
- **Tags**: docs
```tsx
import { VisaErrorTiny } from '@visa/nova-icons-react';
import { Button, InputContainer, InputMessage, Label, Textarea, Utility, UtilityFragment } from '@visa/nova-react';
import { ChangeEvent, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'text-count-textarea';
const maxCharacters = 400;

const getMessage = ({
  characterCount,
  characterCountInvalid,
  invalid,
}: {
  characterCount: number;
  characterCountInvalid: boolean;
  invalid: boolean;
}) => {
  if (invalid) return 'This is a required field';
  if (characterCountInvalid)
    return `${characterCount - maxCharacters} character${characterCount - maxCharacters !== 1 ? 's' : ''} over limit`;
  return `${maxCharacters - characterCount} character${maxCharacters - characterCount !== 1 ? 's' : ''} remaining`;
};

export const TextCountTextarea = () => {
  const [invalid, setInvalid] = useState(false);
  const [text, setText] = useState('');

  const characterCount = text.length;
  const characterCountInvalid = characterCount > maxCharacters;
  const messageIsError = characterCountInvalid || invalid;

  const message = getMessage({ characterCount, characterCountInvalid, invalid });

  const onReset = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setInvalid(false);
    setText('');
  };
  const onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setInvalid(characterCount === 0);
  };
  const onTextChange = (e: ChangeEvent<HTMLInputElement>) => {
    setInvalid(false);
    setText(e.target.value);
  };

  return (
    <form onReset={onReset} onSubmit={onSubmit}>
      <Utility vFlex vFlexCol vGap={4}>
        <Label htmlFor={id}>Label (required)</Label>
        <InputContainer className="v-flex-row">
          <Textarea
            aria-describedby={`${id}-message`}
            aria-invalid={characterCountInvalid || invalid}
            aria-required="true"
            fixed
            id={id}
            name={id}
            onChange={onTextChange}
            style={{ blockSize: '130px' }}
            value={text}
          />
        </InputContainer>
        <UtilityFragment vFlex vFlexRow>
          <InputMessage
            aria-atomic={messageIsError}
            aria-live={messageIsError ? 'assertive' : 'polite'}
            id={`${id}-message`}
            role={messageIsError ? 'alert' : undefined}
          >
            {messageIsError && <VisaErrorTiny />}
            {message}
          </InputMessage>
        </UtilityFragment>
      </Utility>
      <Utility vFlex vFlexRow vGap={8} vMarginTop={16}>
        <Button type="submit">Submit</Button>
        <Button colorScheme="secondary" type="reset">
          Reset
        </Button>
      </Utility>
    </form>
  );
};

```

### Textarea with native rows attribute
- **Section**: Multi-line inputs
- **URL**: components/input/native-row-textarea
- **Tags**: 
```tsx
import { InputContainer, Label, Textarea, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'text-area-native-row';

export const NativeRowTextarea = () => {
  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer className="v-flex-row">
        <Textarea aria-required="true" fixed id={id} name={id} rows={3} />
      </InputContainer>
    </Utility>
  );
};

```

### Input with inline label and message
- **Section**: Custom inputs
- **URL**: components/input/custom-inline-label-input
- **Tags**: custom
```tsx
import { Input, InputContainer, InputMessage, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'input-custom-inline-label';

export const CustomInlineLabelInput = () => {
  return (
    <Utility vAlignItems="start" vFlex vFlexRow vGap={4}>
      <Label htmlFor={id} style={{ lineHeight: 'var(--v-input-container-block-size)' }}>
        Label (required)
      </Label>
      <Utility vFlex vFlexCol vGap={4} vFlexGrow>
        <InputContainer>
          <Input aria-describedby={`${id}-message`} aria-required="true" id={id} type="text" />
        </InputContainer>
        <InputMessage id={`${id}-message`}>This is optional text that describes the label in more detail.</InputMessage>
      </Utility>
    </Utility>
  );
};

```

### Input with form control
- **Section**: Custom inputs
- **URL**: components/input/custom-form-input
- **Tags**: custom
```tsx
import { Button, Input, InputContainer, Label, Utility } from '@visa/nova-react';
import { FormEvent } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'input-form-control';

export const CustomFormInput = () => {
  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const query = formData.get(id);
    alert(`${query} submitted!`);
  };
  return (
    <form onSubmit={onSubmit}>
      <Utility vFlex vFlexCol vGap={4}>
        <Label htmlFor={id}>Label (required)</Label>
        <InputContainer>
          <Input aria-required="true" id={id} name={id} type="text" />
        </InputContainer>
      </Utility>
      <Utility vFlex vFlexRow vGap={8} vMarginTop={16}>
        <Button type="submit">Submit</Button>
        <Button colorScheme="secondary" type="reset">
          Reset
        </Button>
      </Utility>
    </form>
  );
};

```

### CVV input
- **Section**: Custom inputs
- **URL**: components/input/cvv-input
- **Tags**: custom
```tsx
import { VisaErrorTiny } from '@visa/nova-icons-react';
import { Button, Input, InputContainer, InputMessage, Label, Utility } from '@visa/nova-react';
import { FormEvent, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'cvv-input';

const cvvLength = 3;

export const CVVInput = () => {
  const [invalid, setInvalid] = useState(false);
  const [focused, setFocused] = useState(false);

  const onReset = () => {
    setInvalid(false);
  };
  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const isValid = event.currentTarget.checkValidity();
    const formData = new FormData(event.currentTarget);
    const formDataObject = Object.fromEntries(formData.entries());

    // If valid, alert with CVV
    if (isValid) alert(`Success!\nCVV: ${formDataObject['cvv-input']}`);
    // If invalid, focus on invalid element
    else (event.currentTarget.querySelector(':invalid') as HTMLInputElement)?.focus();

    setInvalid(!isValid);
  };

  return (
    <Utility noValidate onReset={onReset} onSubmit={onSubmit} tag="form" vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Security code</Label>
      <InputContainer>
        <Input
          aria-describedby={`${id}-message`}
          aria-invalid={invalid}
          aria-required="true"
          autoComplete="cc-csc"
          id={id}
          maxLength={cvvLength}
          name={id}
          onBlur={() => setFocused(false)}
          onFocus={() => setFocused(true)}
          pattern={`[0-9]{${cvvLength}}`}
          required
          type={focused ? 'text' : 'password'}
        />
      </InputContainer>
      {invalid && (
        <InputMessage id={`${id}-message`}>
          <VisaErrorTiny />
          Please choose a valid security code.
        </InputMessage>
      )}
      <Utility vFlex vFlexRow vGap={8} vMarginTop={16}>
        <Button type="submit">Submit</Button>
        <Button colorScheme="secondary" type="reset">
          Reset
        </Button>
      </Utility>
    </Utility>
  );
};

```

## Property Sections
### Input
- **Selector**: <Input />
- **Description**: Text fields that enable users to enter free-form content.

### InputContainer
- **Selector**: <InputContainer />
- **Description**: Container for styling input elements.

### InputControl
- **Selector**: <InputControl />
- **Description**: Container for icons controlling form elements, such as a dropdown icon for a select element.

### InputMessage
- **Selector**: <InputMessage />
- **Description**: Message shown beneath input components to provide context or guidance.

## Properties
### otp
- **Section**: Input
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: one-time pass-code style

### ref
- **Section**: Input
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Input
- **Type**: ElementType
- **Default**: input
- **Required**: false
- **Description**: Tag of Component

### ref
- **Section**: InputContainer
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### surfaceType
- **Section**: InputContainer
- **Type**: "alternate"
- **Default**: 
- **Required**: false
- **Description**: Type of Surface

### tag
- **Section**: InputContainer
- **Type**: ElementType
- **Default**: 
- **Required**: false
- **Description**: Tag of Component

### ref
- **Section**: InputControl
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: InputControl
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of Component

### colorScheme
- **Section**: InputMessage
- **Type**: "default" , "subtle" , "active" , "on-active"
- **Default**: 
- **Required**: false
- **Description**: Color variant

### ref
- **Section**: InputMessage
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: InputMessage
- **Type**: ElementType
- **Default**: span
- **Required**: false
- **Description**: Tag of Component

