# toggle

## Metadata
- **Version**: 0.0.1
- **Description**: Selection element that allows users to switch between states or views.
- **Category**: components

## Example Sections
1. **Single-select toggle buttons**
   - Description: 
2. **Multi-select toggle buttons**
   - Description: 
3. **Custom toggle buttons**
   - Description: 

## Examples
### Single-select toggles
- **Section**: Single-select toggle buttons
- **URL**: components/toggle-button/default-toggles
- **Tags**: 
```tsx
import { Toggle, ToggleContainer, UtilityFragment } from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-toggle';

const options = [
  { label: 'Label 1', id: `${id}-label-1`, defaultSelected: true },
  { label: 'Label 2', id: `${id}-label-2` },
  { label: 'Label 3', id: `${id}-label-3` },
];

export const DefaultToggles = () => {
  const [togglePressedState, setTogglePressedState] = useState(options.map(o => !!o.defaultSelected));

  const handleSingleSelectTogglePress = (pressedIndex: number) => {
    setTogglePressedState(options.map((_, buttonIndex) => pressedIndex === buttonIndex));
  };

  return (
    <ToggleContainer>
      {options.map((option, optionIndex) => (
        <UtilityFragment key={option.id} vGap={6}>
          <Toggle
            tag="button"
            aria-pressed={togglePressedState[optionIndex]}
            onClick={() => handleSingleSelectTogglePress(optionIndex)}
          >
            {option.label}
          </Toggle>
        </UtilityFragment>
      ))}
    </ToggleContainer>
  );
};

```

### Single-select toggles with leading icon
- **Section**: Single-select toggle buttons
- **URL**: components/toggle-button/leading-icon-toggles
- **Tags**: 
```tsx
import { VisaMapLocationTiny, VisaViewGridTiny, VisaViewListTiny } from '@visa/nova-icons-react';
import { Toggle, ToggleContainer, UtilityFragment } from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'leading-icon-toggle';

const options = [
  { label: 'Label 1', id: `${id}-label-1`, icon: <VisaMapLocationTiny />, defaultSelected: true },
  { label: 'Label 2', id: `${id}-label-2`, icon: <VisaViewListTiny /> },
  { label: 'Label 3', id: `${id}-label-3`, icon: <VisaViewGridTiny /> },
];

export const LeadingIconToggles = () => {
  const [togglePressedState, setTogglePressedState] = useState(options.map(o => !!o.defaultSelected));

  const handleSingleSelectTogglePress = (pressedIndex: number) => {
    setTogglePressedState(options.map((_, buttonIndex) => pressedIndex === buttonIndex));
  };

  return (
    <ToggleContainer>
      {options.map((option, optionIndex) => (
        <UtilityFragment key={option.id} vGap={6}>
          <Toggle
            tag="button"
            aria-pressed={togglePressedState[optionIndex]}
            onClick={() => handleSingleSelectTogglePress(optionIndex)}
          >
            {option.icon}
            {option.label}
          </Toggle>
        </UtilityFragment>
      ))}
    </ToggleContainer>
  );
};

```

### Single-select toggles with trailing icon
- **Section**: Single-select toggle buttons
- **URL**: components/toggle-button/trailing-icon-toggles
- **Tags**: 
```tsx
import { VisaMapLocationTiny, VisaViewGridTiny, VisaViewListTiny } from '@visa/nova-icons-react';
import { Toggle, ToggleContainer, UtilityFragment } from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'trailing-icon-toggles';

const options = [
  { label: 'Label 1', id: `${id}-label-1`, icon: <VisaMapLocationTiny />, defaultSelected: true },
  { label: 'Label 2', id: `${id}-label-2`, icon: <VisaViewListTiny /> },
  { label: 'Label 3', id: `${id}-label-3`, icon: <VisaViewGridTiny /> },
];

export const TrailingIconToggles = () => {
  const [togglePressedState, setTogglePressedState] = useState(options.map(o => !!o.defaultSelected));

  const handleSingleSelectTogglePress = (pressedIndex: number) => {
    setTogglePressedState(options.map((_, buttonIndex) => pressedIndex === buttonIndex));
  };

  return (
    <ToggleContainer>
      {options.map((option, optionIndex) => (
        <UtilityFragment key={option.id} vGap={6}>
          <Toggle
            tag="button"
            aria-pressed={togglePressedState[optionIndex]}
            onClick={() => handleSingleSelectTogglePress(optionIndex)}
          >
            {option.label}
            {option.icon}
          </Toggle>
        </UtilityFragment>
      ))}
    </ToggleContainer>
  );
};

```

### Single-select toggles with icon only
- **Section**: Single-select toggle buttons
- **URL**: components/toggle-button/icon-only-toggles
- **Tags**: 
```tsx
import { VisaMapLocationTiny, VisaViewGridTiny, VisaViewListTiny } from '@visa/nova-icons-react';
import { Toggle, ToggleContainer, UtilityFragment } from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'icon-only-toggles';

const options = [
  { label: 'Label 1', id: `${id}-label-1`, icon: <VisaMapLocationTiny />, defaultSelected: true },
  { label: 'Label 2', id: `${id}-label-2`, icon: <VisaViewListTiny /> },
  { label: 'Label 3', id: `${id}-label-3`, icon: <VisaViewGridTiny /> },
];

export const IconOnlyToggles = () => {
  const [togglePressedState, setTogglePressedState] = useState(options.map(o => !!o.defaultSelected));

  const handleSingleSelectTogglePress = (pressedIndex: number) => {
    setTogglePressedState(options.map((_, buttonIndex) => pressedIndex === buttonIndex));
  };

  return (
    <ToggleContainer>
      {options.map((option, optionIndex) => (
        <UtilityFragment key={option.id} vGap={6}>
          <Toggle
            tag="button"
            aria-label={option.label}
            aria-pressed={togglePressedState[optionIndex]}
            onClick={() => handleSingleSelectTogglePress(optionIndex)}
          >
            {option.icon}
          </Toggle>
        </UtilityFragment>
      ))}
    </ToggleContainer>
  );
};

```

### Disabled toggles
- **Section**: Single-select toggle buttons
- **URL**: components/toggle-button/disabled-toggles
- **Tags**: 
```tsx
import { VisaMapLocationTiny, VisaViewGridTiny, VisaViewListTiny } from '@visa/nova-icons-react';
import { Toggle, ToggleContainer, UtilityFragment } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'disabled-toggles';

const options = [
  { label: 'Label 1', id: `${id}-label-1`, icon: <VisaMapLocationTiny />, disabled: true },
  { label: 'Label 2', id: `${id}-label-2`, icon: <VisaViewListTiny />, disabled: true },
  { label: 'Label 3', id: `${id}-label-3`, icon: <VisaViewGridTiny />, disabled: true },
];

export const DisabledToggles = () => {
  return (
    <ToggleContainer>
      {options.map(option => (
        <UtilityFragment key={option.id} vGap={6}>
          <Toggle tag="button" disabled={option.disabled}>
            {option.icon}
            {option.label}
          </Toggle>
        </UtilityFragment>
      ))}
    </ToggleContainer>
  );
};


```

### Disabled and active toggles
- **Section**: Single-select toggle buttons
- **URL**: components/toggle-button/disabled-and-active-toggles
- **Tags**: 
```tsx
import { VisaMapLocationTiny, VisaViewGridTiny, VisaViewListTiny } from '@visa/nova-icons-react';
import { Toggle, ToggleContainer, UtilityFragment } from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'disabled-and-active-toggles';

const options = [
  { label: 'Label 1', id: `${id}-label-1`, icon: <VisaMapLocationTiny />, disabled: false, defaultSelected: true },
  { label: 'Label 2', id: `${id}-label-2`, icon: <VisaViewListTiny />, disabled: false },
  { label: 'Label 3', id: `${id}-label-3`, icon: <VisaViewGridTiny />, disabled: true },
];

export const DisabledAndActiveToggles = () => {
  const [togglePressedState, setTogglePressedState] = useState(options.map(o => !!o.defaultSelected));

  const handleSingleSelectTogglePress = (pressedIndex: number) => {
    setTogglePressedState(options.map((_, buttonIndex) => pressedIndex === buttonIndex));
  };

  return (
    <ToggleContainer>
      {options.map((option, optionIndex) => (
        <UtilityFragment key={option.id} vGap={6}>
          <Toggle
            tag="button"
            aria-pressed={togglePressedState[optionIndex]}
            onClick={() => handleSingleSelectTogglePress(optionIndex)}
            disabled={option.disabled}
          >
            {option.icon}
            {option.label}
          </Toggle>
        </UtilityFragment>
      ))}
    </ToggleContainer>
  );
};

```

### Multi-select toggles
- **Section**: Multi-select toggle buttons
- **URL**: components/toggle-button/multi-select-toggles
- **Tags**: 
```tsx
import { VisaMapLocationLow, VisaViewGridLow, VisaViewListLow } from '@visa/nova-icons-react';
import { Toggle, ToggleContainer, UtilityFragment } from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'multi-select-toggles';

const options = [
  { id: `${id}-label-1`, label: 'Label 1', icon: <VisaMapLocationLow />, defaultSelected: true },
  { id: `${id}-label-2`, label: 'Label 2', icon: <VisaViewListLow /> },
  { id: `${id}-label-3`, label: 'Label 3', icon: <VisaViewGridLow />, defaultSelected: true },
];

export const MultiSelectToggles = () => {
  const [togglePressedState, setTogglePressedState] = useState(options.map(o => !!o.defaultSelected));

  const handleSingleSelectTogglePress = (pressedIndex: number) => {
    setTogglePressedState(prevState => {
      return prevState.map((buttonSelected, buttonIndex) =>
        pressedIndex === buttonIndex ? !buttonSelected : buttonSelected
      );
    });
  };

  return (
    <ToggleContainer>
      {options.map((option, optionIndex) => (
        <UtilityFragment key={option.id} vGap={6}>
          <Toggle
            tag="button"
            aria-label={option.label}
            aria-pressed={togglePressedState[optionIndex]}
            onClick={() => handleSingleSelectTogglePress(optionIndex)}
          >
            {option.icon}
          </Toggle>
        </UtilityFragment>
      ))}
    </ToggleContainer>
  );
};

```

### Standalone multi-select toggle
- **Section**: Multi-select toggle buttons
- **URL**: components/toggle-button/standalone-multi-select-toggle
- **Tags**: 
```tsx
import { VisaMapLocationLow } from '@visa/nova-icons-react';
import { Toggle, ToggleContainer, UtilityFragment } from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'standalone-multi-select-toggle';

export const StandaloneMultiSelectToggle = () => {
  const [togglePressedState, setTogglePressedState] = useState<boolean>(false);

  const handleTogglePress = () => {
    setTogglePressedState(prevState => !prevState);
  };

  return (
    <ToggleContainer>
      <UtilityFragment vGap={6}>
        <Toggle id={id} tag="button" aria-label="Label 1" aria-pressed={togglePressedState} onClick={handleTogglePress}>
          <VisaMapLocationLow />
        </Toggle>
      </UtilityFragment>
    </ToggleContainer>
  );
};

```

### Single-select toggles using radio buttons
- **Section**: Custom toggle buttons
- **URL**: components/toggle-button/single-select-radio-toggles
- **Tags**: 
```tsx
import { Radio, Toggle, ToggleContainer } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'single-select-radio-toggles';

const options = [
  { id: `${id}-label-1`, label: 'Label 1', defaultSelected: true },
  { id: `${id}-label-2`, label: 'Label 2' },
  { id: `${id}-label-3`, label: 'Label 3' },
];

export const SingleSelectRadioToggles = () => {
  return (
    <ToggleContainer>
      {options.map((option, index) => (
        <Toggle className="v-gap-6" htmlFor={option.id} key={`${id}-option-${index}`}>
          <Radio defaultChecked={option.defaultSelected} id={option.id} name={`${id}-options`} />
          {option.label}
        </Toggle>
      ))}
    </ToggleContainer>
  );
};

```

### Multi-select toggles using checkboxes
- **Section**: Custom toggle buttons
- **URL**: components/toggle-button/multi-select-checkbox-toggles
- **Tags**: 
```tsx
import { VisaMapLocationLow, VisaViewGridLow, VisaViewListLow } from '@visa/nova-icons-react';
import { Checkbox, Toggle, ToggleContainer } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'multi-select-checkbox-toggle';

const options = [
  { id: `${id}-label-1`, label: 'Label 1', icon: <VisaMapLocationLow />, checked: true },
  { id: `${id}-label-2`, label: 'Label 2', icon: <VisaViewListLow />, checked: false },
  { id: `${id}-label-3`, label: 'Label 3', icon: <VisaViewGridLow />, checked: true },
];

export const MultiSelectCheckboxToggles = () => {
  return (
    <ToggleContainer>
      {options.map(({ label, icon, checked }, index) => (
        <Toggle className="v-gap-6" aria-label={label} htmlFor={`${id}-option-${index}`} key={`${id}-option-${index}`}>
          <Checkbox defaultChecked={checked} id={`${id}-option-${index}`} name={`${id}-options`} /> {icon}
        </Toggle>
      ))}
    </ToggleContainer>
  );
};

```

## Property Sections
### Toggle
- **Selector**: <Toggle />
- **Description**: Selection element that allows users to switch between states or views.

### ToggleContainer
- **Selector**: <ToggleContainer />
- **Description**: Element to contain a group of toggle components.

## Properties
### iconOnly
- **Section**: Toggle
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icons only toggle button

### ref
- **Section**: Toggle
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Toggle
- **Type**: ElementType
- **Default**: label
- **Required**: false
- **Description**: Tag of Component

### ref
- **Section**: ToggleContainer
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: ToggleContainer
- **Type**: ElementType
- **Default**: fieldset
- **Required**: false
- **Description**: Tag of Component

