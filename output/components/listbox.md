# listbox

## Metadata
- **Version**: 0.0.1
- **Description**: Container that displays a list of items available for selection.
- **Category**: components

## Example Sections
1. **Single-select listboxes**
   - Description: 
2. **Multi-select listboxes**
   - Description: 
3. **Custom listboxes**
   - Description: 

## Examples
### Default single-select listbox
- **Section**: Single-select listboxes
- **URL**: components/listbox/default-single-listbox
- **Tags**: 
```tsx
import { Label, Listbox, ListboxContainer, ListboxItem, Radio } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-single-select-listbox';

const options = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F', 'Item G'];

export const DefaultSingleListbox = () => {
  return (
    <fieldset>
      <Label id={`${id}-legend`} tag="legend">
        Label (required)
      </Label>
      <ListboxContainer>
        <Listbox id={id} scroll tag="div">
          {options.map((option, index) => (
            <ListboxItem htmlFor={`${id}-option-${index}`} key={`${id}-option-${index}`} tag="label">
              <Radio className="v-flex-shrink-0" id={`${id}-option-${index}`} name={`${id}-options`} />
              <Label tag="span">{option}</Label>
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </fieldset>
  );
};

```

### Single-select listbox with inline message
- **Section**: Single-select listboxes
- **URL**: components/listbox/inline-single-listbox
- **Tags**: 
```tsx
import { InputMessage, Label, Listbox, ListboxContainer, ListboxItem, Radio } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'inline-single-select-listbox';

const options = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F', 'Item G'];

export const InlineSingleListbox = () => {
  return (
    <fieldset>
      <Label id={`${id}-legend`} tag="legend">
        Label (required)
      </Label>
      <ListboxContainer>
        <Listbox id={id} scroll tag="div">
          {options.map((option, index) => (
            <ListboxItem htmlFor={`${id}-option-${index}`} key={`${id}-option-${index}`} tag="label">
              <Radio className="v-flex-shrink-0" id={`${id}-option-${index}`} name={`${id}-options`} />
              <Label tag="span">{option}</Label>
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
      <InputMessage id={`${id}-message`}>This is optional text that describes the label in more detail.</InputMessage>
    </fieldset>
  );
};

```

### Single-select listbox with selected item
- **Section**: Single-select listboxes
- **URL**: components/listbox/selected-single-listbox
- **Tags**: 
```tsx
import { Label, Listbox, ListboxContainer, ListboxItem, Radio } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'selected-single-select-listbox';

const options = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F', 'Item G'];

export const SelectedSingleListbox = () => {
  return (
    <fieldset>
      <Label id={`${id}-legend`} tag="legend">
        Label (required)
      </Label>
      <ListboxContainer>
        <Listbox id={id} scroll tag="div">
          {options.map((option, index) => (
            <ListboxItem htmlFor={`${id}-option-${index}`} key={`${id}-option-${index}`} tag="label">
              <Radio
                className="v-flex-shrink-0"
                defaultChecked={index === 1}
                id={`${id}-option-${index}`}
                name={`${id}-option-${index}`}
              />
              <Label tag="span">{option}</Label>
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </fieldset>
  );
};

```

### Single-select listbox with resize property
- **Section**: Single-select listboxes
- **URL**: components/listbox/resize-single-listbox
- **Tags**: 
```tsx
import { Label, Listbox, ListboxContainer, ListboxItem, Radio } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'resize-single-select-listbox';

const options = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F', 'Item G'];

export const ResizeSingleListbox = () => {
  return (
    <fieldset>
      <Label id={`${id}-legend`} tag="legend">
        Label (required)
      </Label>
      <ListboxContainer>
        <Listbox id={id} tag="div">
          {options.map((option, index) => (
            <ListboxItem htmlFor={`${id}-option-${index}`} key={`${id}-option-${index}`} tag="label">
              <Radio className="v-flex-shrink-0" id={`${id}-option-${index}`} name={`${id}-option-${index}`} />
              <Label tag="span">{option}</Label>
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </fieldset>
  );
};

```

### Single-select listbox with error
- **Section**: Single-select listboxes
- **URL**: components/listbox/error-single-listbox
- **Tags**: 
```tsx
import { VisaErrorTiny } from '@visa/nova-icons-react';
import { Button, InputMessage, Label, Listbox, ListboxContainer, ListboxItem, Radio, Utility } from '@visa/nova-react';
import { FormEvent, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'error-single-select-listbox';

const options = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F', 'Item G'];

export const ErrorSingleListbox = () => {
  const [selectedIndex, setSelectedIndex] = useState<number>(-1);
  const [invalid, setInvalid] = useState(false);

  const onReset = (event: FormEvent) => {
    event.preventDefault();
    setInvalid(false);
    setSelectedIndex(-1);
  };

  const onSubmit = (event: FormEvent) => {
    event.preventDefault();
    setInvalid(selectedIndex === -1);
  };

  return (
    <form onReset={onReset} onSubmit={onSubmit}>
      <fieldset aria-invalid={invalid}>
        <Label id={`${id}-legend`} tag="legend">
          Label (required)
        </Label>
        <ListboxContainer error={invalid}>
          <Listbox id={id} scroll tag="div">
            {options.map((option, index) => (
              <ListboxItem htmlFor={`${id}-option-${index}`} key={`${id}-option-${index}`} tag="label">
                <Radio
                  checked={selectedIndex === index}
                  className="v-flex-shrink-0"
                  id={`${id}-option-${index}`}
                  name={`${id}-options`}
                  onChange={() => setSelectedIndex(index)}
                />
                <Label tag="span">{option}</Label>
              </ListboxItem>
            ))}
          </Listbox>
        </ListboxContainer>
        {invalid && (
          <InputMessage id={`${id}-message`}>
            <VisaErrorTiny />
            This is required text that describes the error in more detail.
          </InputMessage>
        )}
      </fieldset>

      <Utility vFlex vFlexRow vGap={8}>
        <Utility element={<Button type="submit" />} vMarginTop={8}>
          Submit
        </Utility>
        <Utility element={<Button colorScheme="secondary" type="reset" />} vMarginTop={8}>
          Reset
        </Utility>
      </Utility>
    </form>
  );
};

```

### Disabled single-select listbox
- **Section**: Single-select listboxes
- **URL**: components/listbox/disabled-single-listbox
- **Tags**: 
```tsx
import { Label, Listbox, ListboxContainer, ListboxItem, Radio } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'disabled-single-select-listbox';

const options = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F', 'Item G'];

export const DisabledSingleListbox = () => {
  return (
    <fieldset>
      <Label id={`${id}-legend`} tag="legend">
        Label (required)
      </Label>
      <ListboxContainer disabled>
        <Listbox id={id} scroll tag="div">
          {options.map((option, index) => (
            <ListboxItem htmlFor={`${id}-option-${index}`} key={`${id}-option-${index}`} tag="label">
              <Radio className="v-flex-shrink-0" disabled id={`${id}-option-${index}`} name={`${id}-options`} />
              <Label tag="span">{option}</Label>
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </fieldset>
  );
};

```

### Single-select listbox with disabled item
- **Section**: Single-select listboxes
- **URL**: components/listbox/item-disabled-single-listbox
- **Tags**: 
```tsx
import { Label, Listbox, ListboxContainer, ListboxItem, Radio } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'item-disabled-single-select-listbox';

const options = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F', 'Item G'];

export const ItemDisabledSingleListbox = () => {
  return (
    <fieldset>
      <Label id={`${id}-legend`} tag="legend">
        Label (required)
      </Label>
      <ListboxContainer>
        <Listbox id={id} scroll tag="div">
          {options.map((option, index) => (
            <ListboxItem htmlFor={`${id}-option-${index}`} key={`${id}-option-${index}`} tag="label">
              <Radio
                className="v-flex-shrink-0"
                disabled={index === 1}
                id={`${id}-option-${index}`}
                name={`${id}-options`}
              />
              <Label tag="span">{option}</Label>
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </fieldset>
  );
};

```

### Default multi-select listbox
- **Section**: Multi-select listboxes
- **URL**: components/listbox/default-multi-listbox
- **Tags**: 
```tsx
import { Checkbox, Label, Listbox, ListboxContainer, ListboxItem } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-multi-select-listbox';

const options = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F', 'Item G'];

export const DefaultMultiListbox = () => {
  return (
    <fieldset>
      <Label id={`${id}-legend`} tag="legend">
        Label (required)
      </Label>
      <ListboxContainer>
        <Listbox id={id} scroll tag="div">
          {options.map((option, index) => (
            <ListboxItem htmlFor={`${id}-option-${index}`} key={`${id}-option-${index}`} tag="label">
              <Checkbox className="v-flex-shrink-0" id={`${id}-option-${index}`} name={`${id}-option-${index}`} />
              <Label tag="span">{option}</Label>
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </fieldset>
  );
};

```

### Multi-select listbox with inline message
- **Section**: Multi-select listboxes
- **URL**: components/listbox/inline-multi-listbox
- **Tags**: 
```tsx
import { Checkbox, InputMessage, Label, Listbox, ListboxContainer, ListboxItem } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'inline-multi-select-listbox';

const options = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F', 'Item G'];

export const InlineMultiListbox = () => {
  return (
    <fieldset>
      <Label id={`${id}-legend`} tag="legend">
        Label (required)
      </Label>
      <ListboxContainer>
        <Listbox id={id} scroll tag="div">
          {options.map((option, index) => (
            <ListboxItem htmlFor={`${id}-option-${index}`} key={`${id}-option-${index}`} tag="label">
              <Checkbox className="v-flex-shrink-0" id={`${id}-option-${index}`} name={`${id}-option-${index}`} />
              <Label tag="span">{option}</Label>
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
      <InputMessage id={`${id}-message`}>This is optional text that describes the label in more detail.</InputMessage>
    </fieldset>
  );
};

```

### Multi-select listbox with selected item
- **Section**: Multi-select listboxes
- **URL**: components/listbox/selected-multi-listbox
- **Tags**: 
```tsx
import { Checkbox, Label, Listbox, ListboxContainer, ListboxItem } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'selected-multi-select-listbox';

const options = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F', 'Item G'];

export const SelectedMultiListbox = () => {
  return (
    <fieldset>
      <Label id={`${id}-legend`} tag="legend">
        Label (required)
      </Label>
      <ListboxContainer>
        <Listbox id={id} scroll tag="div">
          {options.map((option, index) => (
            <ListboxItem htmlFor={`${id}-option-${index}`} key={`${id}-option-${index}`} tag="label">
              <Checkbox
                className="v-flex-shrink-0"
                defaultChecked={index === 1}
                id={`${id}-option-${index}`}
                name={`${id}-option-${index}`}
              />
              <Label tag="span">{option}</Label>
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </fieldset>
  );
};

```

### Multi-select listbox with resize property
- **Section**: Multi-select listboxes
- **URL**: components/listbox/resize-multi-listbox
- **Tags**: 
```tsx
import { Checkbox, Label, Listbox, ListboxContainer, ListboxItem } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'resize-multi-select-listbox';

const options = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F', 'Item G'];

export const ResizeMultiListbox = () => {
  return (
    <fieldset>
      <Label id={`${id}-legend`} tag="legend">
        Label (required)
      </Label>
      <ListboxContainer>
        <Listbox id={id} tag="div">
          {options.map((option, index) => (
            <ListboxItem htmlFor={`${id}-option-${index}`} key={`${id}-option-${index}`} tag="label">
              <Checkbox className="v-flex-shrink-0" id={`${id}-option-${index}`} name={`${id}-option-${index}`} />
              <Label tag="span">{option}</Label>
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </fieldset>
  );
};

```

### Multi-select listbox with error
- **Section**: Multi-select listboxes
- **URL**: components/listbox/error-multi-listbox
- **Tags**: 
```tsx
import { VisaErrorTiny } from '@visa/nova-icons-react';
import {
  Button,
  Checkbox,
  InputMessage,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Utility,
} from '@visa/nova-react';
import { FormEvent, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'error-multi-select-listbox';

const options = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F', 'Item G'];

export const ErrorMultiListbox = () => {
  const [selectedIndexes, setSelectedIndexes] = useState<Record<number, boolean>>({});
  const [invalid, setInvalid] = useState(false);

  const onSelectionChange = (e: FormEvent<HTMLInputElement>, index: number) => {
    const newSelectedIndexes = { ...selectedIndexes };
    newSelectedIndexes[index] = e.currentTarget.checked;
    setSelectedIndexes(newSelectedIndexes);
  };

  const onReset = (event: FormEvent) => {
    event.preventDefault();
    setInvalid(false);
    setSelectedIndexes({});
  };

  const onSubmit = (event: FormEvent) => {
    event.preventDefault();
    // If there isn't a card selected, set invalid to true
    const invalid = !Object.values(selectedIndexes).some(selectedCard => selectedCard);
    setInvalid(invalid);
  };

  return (
    <form onSubmit={onSubmit} onReset={onReset}>
      <fieldset aria-invalid={invalid}>
        <Label id={`${id}-legend`} tag="legend">
          Label (required)
        </Label>
        <ListboxContainer error={invalid}>
          <Listbox id={id} scroll tag="div">
            {options.map((option, index) => (
              <ListboxItem htmlFor={`${id}-option-${index}`} key={`${id}-option-${index}`} tag="label">
                <Checkbox
                  checked={selectedIndexes[index] || false}
                  className="v-flex-shrink-0"
                  id={`${id}-option-${index}`}
                  name={`${id}-options`}
                  onChange={e => onSelectionChange(e, index)}
                />
                <Label tag="span">{option}</Label>
              </ListboxItem>
            ))}
          </Listbox>
        </ListboxContainer>
        {invalid && (
          <InputMessage id={`${id}-message`}>
            <VisaErrorTiny />
            This is required text that describes the error in more detail.
          </InputMessage>
        )}
      </fieldset>
      <Utility vFlex vFlexRow vGap={8}>
        <Utility element={<Button type="submit" />} vMarginTop={8}>
          Submit
        </Utility>
        <Utility element={<Button colorScheme="secondary" type="reset" />} vMarginTop={8}>
          Reset
        </Utility>
      </Utility>
    </form>
  );
};

```

### Disabled multi-select listbox
- **Section**: Multi-select listboxes
- **URL**: components/listbox/disabled-multi-listbox
- **Tags**: 
```tsx
import { Checkbox, Label, Listbox, ListboxContainer, ListboxItem } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'disabled-multi-select-listbox';

const options = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F', 'Item G'];

export const DisabledMultiListbox = () => {
  return (
    <fieldset>
      <Label id={`${id}-legend`} tag="legend">
        Label (required)
      </Label>
      <ListboxContainer disabled>
        <Listbox id={id} scroll tag="div">
          {options.map((option, index) => (
            <ListboxItem htmlFor={`${id}-option-${index}`} key={`${id}-option-${index}`} tag="label">
              <Checkbox
                className="v-flex-shrink-0"
                disabled
                id={`${id}-option-${index}`}
                name={`${id}-option-${index}`}
              />
              <Label tag="span">{option}</Label>
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </fieldset>
  );
};

```

### Multi-select listbox with disabled item
- **Section**: Multi-select listboxes
- **URL**: components/listbox/item-disabled-multi-listbox
- **Tags**: 
```tsx
import { Checkbox, Label, Listbox, ListboxContainer, ListboxItem } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'item-disabled-multi-select-listbox';

const options = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F', 'Item G'];

export const ItemDisabledMultiListbox = () => {
  return (
    <fieldset>
      <Label id={`${id}-legend`} tag="legend">
        Label (required)
      </Label>
      <ListboxContainer>
        <Listbox id={id} scroll tag="div">
          {options.map((option, index) => (
            <ListboxItem htmlFor={`${id}-option-${index}`} key={`${id}-option-${index}`} tag="label">
              <Checkbox
                className="v-flex-shrink-0"
                disabled={index === 1}
                id={`${id}-option-${index}`}
                name={`${id}-option-${index}`}
              />
              <Label tag="span">{option}</Label>
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </fieldset>
  );
};

```

### Single-select listbox with custom hook
- **Section**: Custom listboxes
- **URL**: components/listbox/option-single-listbox
- **Tags**: 
```tsx
import { Label, Listbox, ListboxContainer, ListboxItem, useListbox } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'option-single-select-listbox';

const options = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F', 'Item G'];

export const OptionSingleListbox = () => {
  const {
    isIndexSelected,
    getTabIndex,
    onKeyNavigation,
    ref: listItemsRef,
    toggleIndexSelected,
  } = useListbox({ defaultSelected: 0 }); // Default to selected on first list item

  return (
    <fieldset>
      <Label id={`${id}-legend`} tag="legend">
        Label (required)
      </Label>
      <ListboxContainer>
        <Listbox aria-labelledby={`${id}-legend`} id={id} onKeyDown={onKeyNavigation} role="listbox" scroll>
          {options.map((option, index) => {
            const disabled = index === 1;
            return (
              <ListboxItem
                aria-disabled={disabled || undefined}
                aria-selected={isIndexSelected(index)}
                key={`${id}-option-${index}`}
                onClick={() => toggleIndexSelected(index)}
                ref={el => {
                  listItemsRef.current[index] = el;
                }}
                role="option"
                tabIndex={getTabIndex(index, disabled)}
              >
                <span className="v-radio v-flex-shrink-0 " />
                {option}
              </ListboxItem>
            );
          })}
        </Listbox>
      </ListboxContainer>
    </fieldset>
  );
};

```

### Multi-select listbox with custom hook
- **Section**: Custom listboxes
- **URL**: components/listbox/option-multi-listbox
- **Tags**: 
```tsx
import { Label, Listbox, ListboxContainer, ListboxItem, useListbox } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'option-multi-select-listbox';

const options = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F', 'Item G'];

export const OptionMultiListbox = () => {
  const {
    isIndexSelected,
    getTabIndex,
    onKeyNavigation,
    ref: listItemsRef,
    toggleIndexSelected,
  } = useListbox({ defaultSelected: [0, 3] }); // Default to active on first list item

  return (
    <fieldset>
      <Label id={`${id}-legend`} tag="legend">
        Label (required)
      </Label>
      <ListboxContainer>
        <Listbox aria-labelledby={`${id}-legend`} id={id} onKeyDown={onKeyNavigation} role="listbox" scroll>
          {options.map((option, index) => {
            const disabled = index === 1;
            return (
              <ListboxItem
                aria-disabled={disabled || undefined}
                aria-selected={isIndexSelected(index)}
                key={`${id}-option-${index}`}
                onClick={() => toggleIndexSelected(index)}
                ref={el => {
                  listItemsRef.current[index] = el;
                }}
                role="option"
                tabIndex={getTabIndex(index, disabled)}
              >
                <span className="v-checkbox v-flex-shrink-0" />
                {option}
              </ListboxItem>
            );
          })}
        </Listbox>
      </ListboxContainer>
    </fieldset>
  );
};

```

## Property Sections
### Listbox
- **Selector**: <Listbox />
- **Description**: Container that displays a list of items available for selection.

### ListboxContainer
- **Selector**: <ListboxContainer />
- **Description**: Container for listbox component.

### ListboxItem
- **Selector**: <ListboxItem />
- **Description**: Container for elements used inside listbox.

### useListbox
- **Selector**: None
- **Description**: This hook is used to manage the selected state and keyboard navigation of listbox component.

## Properties
### multiselect
- **Section**: Listbox
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Multiselect

### ref
- **Section**: Listbox
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### scroll
- **Section**: Listbox
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Scroll

### tag
- **Section**: Listbox
- **Type**: ElementType
- **Default**: ul
- **Required**: false
- **Description**: Tag of Component

### error
- **Section**: ListboxContainer
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Error

### ref
- **Section**: ListboxContainer
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: ListboxContainer
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of Component

### ref
- **Section**: ListboxItem
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: ListboxItem
- **Type**: ElementType
- **Default**: li
- **Required**: false
- **Description**: Tag of Component

