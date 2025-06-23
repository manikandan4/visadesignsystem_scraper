# chip

## Metadata
- **Version**: 0.0.1
- **Description**: Compact elements used to filter content or display user input.
- **Category**: components

## Example Sections
1. **Selection chips**
   - Description: 
2. **Removable chips**
   - Description: 
3. **Custom chips**
   - Description: 

## Examples
### Default selection chip
- **Section**: Selection chips
- **URL**: components/chip/default-selection-chip
- **Tags**: docs
```tsx
import { Checkbox, Chip } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-selection-chip';

export const DefaultSelectionChip = () => {
  return (
    <Chip chipType="selection" htmlFor={id} tag="label">
      Label
      <Checkbox id={id} />
    </Chip>
  );
};

```

### Selected selection chip
- **Section**: Selection chips
- **URL**: components/chip/selected-selection-chip
- **Tags**: docs
```tsx
import { Checkbox, Chip } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'selected-selection-chip';

export const SelectedSelectionChip = () => {
  return (
    <Chip chipType="selection" htmlFor={id} tag="label">
      Label
      <Checkbox defaultChecked id={id} />
    </Chip>
  );
};

```

### Multi-line selection chip
- **Section**: Selection chips
- **URL**: components/chip/multi-line-selection-chip
- **Tags**: docs
```tsx
import { Checkbox, Chip } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'multi-line-selection-chip';

export const MultiLineSelectionChip = () => {
  return (
    <Chip chipType="selection" htmlFor={id} tag="label">
      This is a chip label
      <br />
      that wraps on
      <br />
      multiple lines
      <Checkbox id={id} />
    </Chip>
  );
};

```

### Disabled selection chip
- **Section**: Selection chips
- **URL**: components/chip/disabled-selection-chip
- **Tags**: docs
```tsx
import { Checkbox, Chip } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'disabled-selection-chip';

export const DisabledSelectionChip = () => {
  return (
    <Chip chipType="selection" htmlFor={id} tag="label">
      Label
      <Checkbox disabled id={id} />
    </Chip>
  );
};

```

### Disabled selected selection chip
- **Section**: Selection chips
- **URL**: components/chip/checked-disabled-selection-chip
- **Tags**: 
```tsx
import { Checkbox, Chip } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'checked-disabled-selection-chip';

export const CheckedDisabledSelectionChip = () => {
  return (
    <Chip chipType="selection" htmlFor={id} tag="label">
      Label
      <Checkbox defaultChecked disabled id={id} />
    </Chip>
  );
};

```

### Selection chip group
- **Section**: Selection chips
- **URL**: components/chip/selection-group-chip
- **Tags**: 
```tsx
import { Checkbox, Chip, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'selection-group-chip';

const chips = ['Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5', 'Label 6', 'Label 7'];

export const SelectionGroupChip = () => {
  return (
    <Utility vFlex vFlexWrap vGap={8} style={{ inlineSize: '50%' }}>
      {chips.map((chip, index) => (
        <Chip chipType="selection" htmlFor={`${id}-${index}`} key={`${id}-${index}`} tag="label">
          <span>{chip}</span>
          <Checkbox id={`${id}-${index}`} />
        </Chip>
      ))}
    </Utility>
  );
};

```

### Default removable chip
- **Section**: Removable chips
- **URL**: components/chip/default-removable-chip
- **Tags**: docs
```tsx
import { VisaClearAltTiny } from '@visa/nova-icons-react';
import { Button, Chip } from '@visa/nova-react';

export const DefaultRemovableChip = () => {
  return (
    <Chip>
      <span>Label</span>
      <Button aria-label="clear Label" colorScheme="tertiary" iconButton subtle>
        <VisaClearAltTiny />
      </Button>
    </Chip>
  );
};

```

### Removable chip with icon
- **Section**: Removable chips
- **URL**: components/chip/removable-icon-chip
- **Tags**: docs
```tsx
import { VisaAccountTiny, VisaClearAltTiny } from '@visa/nova-icons-react';
import { Button, Chip } from '@visa/nova-react';

export const RemovableIconChip = () => {
  return (
    <Chip>
      <VisaAccountTiny />
      <span>Label</span>
      <Button aria-label="clear Label" colorScheme="tertiary" iconButton subtle>
        <VisaClearAltTiny />
      </Button>
    </Chip>
  );
};

```

### Removable chip with avatar
- **Section**: Removable chips
- **URL**: components/chip/removable-avatar-chip
- **Tags**: docs
```tsx
import { VisaClearAltTiny } from '@visa/nova-icons-react';
import { Avatar, Button, Chip } from '@visa/nova-react';

/// This is the base url for where your site is deployed. `import.meta.env.BASE_URL` is the environment variable used to import the base url for Vite. Change this import to match your build tool's base url.
const BASE_URL = import.meta.env.BASE_URL;

export const RemovableAvatarChip = () => {
  return (
    <Chip>
      <Avatar aria-label="Alex Miller" src={BASE_URL + '/alex-miller-stock.png'} tag="img" />
      <span>Label</span>
      <Button aria-label="clear Label" colorScheme="tertiary" iconButton subtle>
        <VisaClearAltTiny />
      </Button>
    </Chip>
  );
};

```

### Disabled removable chip
- **Section**: Removable chips
- **URL**: components/chip/disabled-removable-chip
- **Tags**: docs
```tsx
import { VisaClearAltTiny } from '@visa/nova-icons-react';
import { Button, Chip } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'multi-line-selection-chip';

export const DisabledRemovableChip = () => {
  return (
    <Chip>
      <label className="v-label" htmlFor={id}>Label</label> 
      <Button aria-label="clear" colorScheme="tertiary" id={id} disabled iconButton subtle>
        <VisaClearAltTiny />
      </Button>
    </Chip>
  );
};

```

### Compact removable chip
- **Section**: Removable chips
- **URL**: components/chip/compact-removable-chip
- **Tags**: docs
```tsx
import { VisaClearAltTiny } from '@visa/nova-icons-react';
import { Button, Chip } from '@visa/nova-react';

export const CompactRemovableChip = () => {
  return (
    <Chip chipSize="compact">
      <span>Label</span>
      <Button aria-label="clear Label" colorScheme="tertiary" iconButton subtle>
        <VisaClearAltTiny />
      </Button>
    </Chip>
  );
};

```

### Compact removable chip with icon
- **Section**: Removable chips
- **URL**: components/chip/compact-removable-icon-chip
- **Tags**: 
```tsx
import { VisaAccountTiny, VisaClearAltTiny } from '@visa/nova-icons-react';
import { Button, Chip } from '@visa/nova-react';

export const CompactRemovableIconChip = () => {
  return (
    <Chip chipSize="compact">
      <VisaAccountTiny />
      <span>Label</span>
      <Button aria-label="clear Label" colorScheme="tertiary" iconButton subtle>
        <VisaClearAltTiny />
      </Button>
    </Chip>
  );
};

```

### Compact removable chip with avatar
- **Section**: Removable chips
- **URL**: components/chip/compact-removable-avatar-chip
- **Tags**: 
```tsx
import { VisaClearAltTiny } from '@visa/nova-icons-react';
import { Avatar, Button, Chip } from '@visa/nova-react';

/// This is the base url for where your site is deployed. `import.meta.env.BASE_URL` is the environment variable used to import the base url for Vite. Change this import to match your build tool's base url.
const BASE_URL = import.meta.env.BASE_URL;

export const CompactRemovableAvatarChip = () => {
  return (
    <Chip chipSize="compact">
      <Avatar aria-label="Alex Miller" src={BASE_URL + '/alex-miller-stock.png'} tag="img" />
      <span>Label</span>
      <Button aria-label="clear Label" colorScheme="tertiary" iconButton subtle>
        <VisaClearAltTiny />
      </Button>
    </Chip>
  );
};

```

### Removable chip group
- **Section**: Removable chips
- **URL**: components/chip/removable-group-chip
- **Tags**: docs
```tsx
import { useState } from 'react';
import { VisaClearAltTiny } from '@visa/nova-icons-react';
import { Button, Chip, Utility } from '@visa/nova-react';

export const RemovableGroupChip = () => {
  const initialChips = ['Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5', 'Label 6', 'Label 7', 'Label 8'];
  const [chips, setChips] = useState(initialChips);

  const handleRemove = (chipToRemove: string) => {
    setChips(chips => chips.filter(chip => chip !== chipToRemove));
  };

  const resetChips = () => {
    setChips(initialChips);
  };

  return (
    <>
      <Utility vFlex vFlexWrap vGap={8}>
        {chips.map((chip, index) => (
          <Chip key={index}>
            {chip}
            <Button iconButton colorScheme="tertiary" subtle aria-label={`Clear ${chip}`} onClick={() => handleRemove(chip)}>
              <VisaClearAltTiny />
            </Button>
          </Chip>
        ))}
      </Utility>
      <Utility vMarginTop={12}>
        <Button onClick={resetChips}>Reset</Button>
      </Utility>
    </>
  );
};

```

### Compact removable chip group
- **Section**: Removable chips
- **URL**: components/chip/compact-removable-group-chip
- **Tags**: docs
```tsx
import { useState } from 'react';
import { VisaClearAltTiny } from '@visa/nova-icons-react';
import { Button, Chip, Utility } from '@visa/nova-react';

export const CompactRemovableGroupChip = () => {
  const initialChips = ['Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5', 'Label 6'];
  const [chips, setChips] = useState(initialChips);

  const handleRemove = (chipToRemove: string) => {
    setChips(chips => chips.filter(chip => chip !== chipToRemove));
  };

  const resetChips = () => {
    setChips(initialChips);
  };

  return (
    <>
      <Utility vFlex vFlexWrap vGap={8}>
        {chips.map((chip, index) => (
          <Chip chipSize="compact" key={index}>
            {chip}
            <Button iconButton colorScheme="tertiary" subtle aria-label={`Clear ${chip}`} onClick={() => handleRemove(chip)}>
              <VisaClearAltTiny />
            </Button>
          </Chip>
        ))}
      </Utility>
      <Utility vMarginTop={12}>
        <Button onClick={resetChips}>Reset</Button>
      </Utility>
    </>
  );
};
```

### Static chip
- **Section**: Custom chips
- **URL**: components/chip/static-chip
- **Tags**: docs
```tsx
import { Chip } from '@visa/nova-react';

export const StaticChip = () => {
  return (
    <Chip tag="label" readOnly>
      Label
    </Chip>
  );
};

```

## Property Sections
### Chip
- **Selector**: <Chip />
- **Description**: Compact elements used to filter content or display user input.

## Properties
### chipSize
- **Section**: Chip
- **Type**: "compact"
- **Default**: 
- **Required**: false
- **Description**: Chip Size

### chipType
- **Section**: Chip
- **Type**: "selection"
- **Default**: 
- **Required**: false
- **Description**: Chip Type

### ref
- **Section**: Chip
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Chip
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of Component

