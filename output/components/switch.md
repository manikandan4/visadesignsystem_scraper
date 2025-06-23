# switch

## Metadata
- **Version**: 0.0.1
- **Description**: Binary control that allows users to toggle between two states, such as on/off.
- **Category**: components

## Example Sections
1. **Default switches**
   - Description: 

## Examples
### Default switch
- **Section**: Default switches
- **URL**: components/switch/default-switch
- **Tags**: 
```tsx
import { Switch, SwitchLabel, Utility } from '@visa/nova-react';

const id = 'default-switch-example';

export const DefaultSwitch = () => {
  return (
    <Utility vFlex vFlexWrap vGap={10} vJustifyContent="between" vMargin={8} style={{ maxInlineSize: '288px' }}>
      <SwitchLabel htmlFor={`${id}-switch`}>Label</SwitchLabel>
      <Switch id={`${id}-switch`} name="default-switch" />
    </Utility>
  );
};

```

### Switch with description
- **Section**: Default switches
- **URL**: components/switch/optional-message-switch
- **Tags**: 
```tsx
import { InputMessage, Switch, SwitchLabel, Utility } from '@visa/nova-react';

const id = 'optional-message-switch-example';

export const OptionalMessageSwitch = () => {
  return (
    <Utility
      vAlignItems="center"
      vFlex
      vFlexRow
      vFlexWrap
      vGap={10}
      vJustifyContent="between"
      vMargin={8}
      style={{ maxInlineSize: '288px' }}
    >
      <Utility vFlex vFlexCol vFlexGrow vGap={2} vJustifyContent="between" style={{ flexBasis: 'min-content' }}>
        <SwitchLabel htmlFor={`${id}-switch`}>Label</SwitchLabel>
        <InputMessage id={`${id}-message`}>
          This is optional text that can be used to describe the label in more detail.
        </InputMessage>
      </Utility>
      <Switch aria-describedby={`${id}-message`} id={`${id}-switch`} name="switch-with-message" />
    </Utility>
  );
};

```

### Disabled switch
- **Section**: Default switches
- **URL**: components/switch/disabled-switch
- **Tags**: 
```tsx
import { Switch, SwitchLabel, Utility } from '@visa/nova-react';

const id = 'disabled-switch-example';

export const DisabledSwitch = () => {
  return (
    <Utility vFlex vFlexWrap vGap={10} vJustifyContent="between" vMargin={8} style={{ maxInlineSize: '288px' }}>
      <SwitchLabel htmlFor={`${id}-switch`}>Label</SwitchLabel>
      <Switch disabled id={`${id}-switch`} name="disabled-off-switch" />
    </Utility>
  );
};

```

### Disabled selected switch
- **Section**: Default switches
- **URL**: components/switch/disabled-switch-on
- **Tags**: 
```tsx
import { Switch, SwitchLabel, Utility } from '@visa/nova-react';

const id = 'disabled-switch-on-example';

export const DisabledSwitchOn = () => {
  return (
    <Utility vFlex vFlexWrap vGap={10} vJustifyContent="between" vMargin={8} style={{ maxInlineSize: '288px' }}>
      <SwitchLabel htmlFor={`${id}-switch`}>Label</SwitchLabel>
      <Switch checked disabled id={`${id}-switch`} name="disabled-switch-on" />
    </Utility>
  );
};

```

## Property Sections
### Switch
- **Selector**: <Switch />
- **Description**: Binary control that allows users to toggle between two states, such as on/off.

### SwitchLabel
- **Selector**: <SwitchLabel />
- **Description**: Label to be used with switch component.

## Properties
### ref
- **Section**: Switch
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Switch
- **Type**: ElementType
- **Default**: input
- **Required**: false
- **Description**: Tag of Component

### ref
- **Section**: SwitchLabel
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: SwitchLabel
- **Type**: ElementType
- **Default**: 
- **Required**: false
- **Description**: Tag of Component

