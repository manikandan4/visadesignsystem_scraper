# combobox

## Metadata
- **Version**: 0.0.1
- **Description**: Dropdown menu enabling users to enter text or select items from a list.
- **Category**: components

## Example Sections
1. **Default Comboboxes**
   - Description: 
2. **Combobox behaviors**
   - Description: 

## Examples
### Default combobox
- **Section**: Default Comboboxes
- **URL**: components/combobox/no-autocomplete-combobox
- **Tags**: docs
```tsx
import { VisaChevronDownTiny } from '@visa/nova-icons-react';
import {
  Button,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Radio,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox } from 'downshift';

type Item = { value: string };

const items: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const stateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) =>
  // this prevents on mouse hover, the item in the list is automatic selected
  type === useCombobox.stateChangeTypes.ItemMouseMove || type === useCombobox.stateChangeTypes.MenuMouseLeave
    ? {
        ...changes, // default Downshift new state changes on item selection.
        highlightedIndex: state.highlightedIndex,
      }
    : changes;

export const NoAutocompleteCombobox = () => {
  const {
    getInputProps,
    getItemProps,
    getLabelProps,
    getMenuProps,
    getToggleButtonProps,
    highlightedIndex,
    inputValue,
    isOpen,
  } = useCombobox({
    items: items,
    itemToString,
    stateReducer,
  });
  const { id: listboxId, ...listboxProps } = getMenuProps();

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label</Label>
          <UtilityFragment vFlexRow>
            <InputContainer>
              <Input
                aria-haspopup="listbox"
                name="text-input-field-1"
                type="text"
                {...getInputProps({ 'aria-expanded': isOpen, 'aria-owns': listboxId })}
              />
              <Button
                aria-label="expand"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                {...getToggleButtonProps()}
              >
                <VisaChevronDownTiny />
              </Button>
            </InputContainer>
          </UtilityFragment>
        </DropdownContainer>
      </UtilityFragment>
      <ListboxContainer>
        <Listbox id={listboxId} {...listboxProps}>
          {items.map((item, index) => (
            <ListboxItem
              className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
              key={`no-autocomplete-example-${index}`}
              {...getItemProps({
                'aria-selected': inputValue === item.value,
                index,
                item,
              })}
            >
              <UtilityFragment vFlexShrink0>
                <Radio tag="span" />
              </UtilityFragment>
              {item.value}
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </Combobox>
  );
};

```

### Combobox with selected option
- **Section**: Default Comboboxes
- **URL**: components/combobox/pre-selected-combobox
- **Tags**: docs
```tsx
import { VisaChevronDownTiny } from '@visa/nova-icons-react';
import {
  Button,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Radio,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox } from 'downshift';

type Item = { value: string };

const items: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const stateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) =>
  // this prevents on mouse hover, the item in the list is automatic selected
  type === useCombobox.stateChangeTypes.ItemMouseMove || type === useCombobox.stateChangeTypes.MenuMouseLeave
    ? {
        ...changes, // default Downshift new state changes on item selection.
        highlightedIndex: state.highlightedIndex,
      }
    : changes;

export const PreSelectedCombobox = () => {
  const {
    getInputProps,
    getItemProps,
    getLabelProps,
    getMenuProps,
    getToggleButtonProps,
    highlightedIndex,
    inputValue,
    isOpen,
  } = useCombobox({
    initialInputValue: 'Option A',
    items: items,
    itemToString,
    stateReducer,
  });
  const { id: listboxId, ...listboxProps } = getMenuProps();

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label</Label>
          <UtilityFragment vFlexRow>
            <InputContainer>
              <Input
                aria-haspopup="listbox"
                name="text-input-field-2"
                type="text"
                {...getInputProps({ 'aria-expanded': isOpen, 'aria-owns': listboxId })}
              />
              <Button
                aria-label="expand"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                {...getToggleButtonProps()}
              >
                <VisaChevronDownTiny />
              </Button>
            </InputContainer>
          </UtilityFragment>
        </DropdownContainer>
      </UtilityFragment>
      <ListboxContainer>
        <Listbox id={listboxId} {...listboxProps}>
          {items.map((item, index) => (
            <ListboxItem
              className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
              key={`pre-selected-example-${index}`}
              {...getItemProps({
                'aria-selected': inputValue === item.value,
                index,
                item,
              })}
            >
              <UtilityFragment vFlexShrink0>
                <Radio tag="span" />
              </UtilityFragment>
              {item.value}
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </Combobox>
  );
};

```

### Combobox with inline message
- **Section**: Default Comboboxes
- **URL**: components/combobox/inline-message-combobox
- **Tags**: docs
```tsx
import { VisaChevronDownTiny } from '@visa/nova-icons-react';
import {
  Button,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  InputMessage,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Radio,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox } from 'downshift';

type Item = { value: string };

const items: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const stateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) =>
  // this prevents on mouse hover, the item in the list is automatic selected
  type === useCombobox.stateChangeTypes.ItemMouseMove || type === useCombobox.stateChangeTypes.MenuMouseLeave
    ? {
        ...changes, // default Downshift new state changes on item selection.
        highlightedIndex: state.highlightedIndex,
      }
    : changes;

export const InlineMessageCombobox = () => {
  const {
    getInputProps,
    getItemProps,
    getLabelProps,
    getMenuProps,
    getToggleButtonProps,
    highlightedIndex,
    inputValue,
    isOpen,
  } = useCombobox({
    items: items,
    itemToString,
    stateReducer,
  });
  const { id: listboxId, ...listboxProps } = getMenuProps();

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label</Label>
          <UtilityFragment vFlexRow>
            <InputContainer>
              <Input
                aria-describedby="combobox-inline-message"
                aria-haspopup="listbox"
                name="text-input-field-3"
                type="text"
                {...getInputProps({ 'aria-expanded': isOpen, 'aria-owns': listboxId })}
              />
              <Button
                aria-label="expand"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                {...getToggleButtonProps()}
              >
                <VisaChevronDownTiny />
              </Button>
            </InputContainer>
          </UtilityFragment>
          {!isOpen && (
            <InputMessage id="combobox-inline-message">
              This is optional text that describes the label in more detail.
            </InputMessage>
          )}
        </DropdownContainer>
      </UtilityFragment>
      <ListboxContainer>
        <Listbox id={listboxId} {...listboxProps}>
          {items.map((item, index) => (
            <ListboxItem
              className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
              key={`inline-message-example-${index}`}
              {...getItemProps({
                'aria-selected': inputValue === item.value,
                index,
                item,
              })}
            >
              <UtilityFragment vFlexShrink0>
                <Radio tag="span" />
              </UtilityFragment>
              {item.value}
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </Combobox>
  );
};

```

### Combobox with clear button
- **Section**: Default Comboboxes
- **URL**: components/combobox/clear-button-combobox
- **Tags**: docs
```tsx
import { VisaChevronDownTiny, VisaChevronUpTiny, VisaClearAltTiny } from '@visa/nova-icons-react';
import {
  Button,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Radio,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox } from 'downshift';
import { FocusEvent, useState } from 'react';

type Item = { value: string };

const items: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const stateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) =>
  // this prevents on mouse hover, the item in the list is automatic selected
  type === useCombobox.stateChangeTypes.ItemMouseMove || type === useCombobox.stateChangeTypes.MenuMouseLeave
    ? {
        ...changes, // default Downshift new state changes on item selection.
        highlightedIndex: state.highlightedIndex,
      }
    : changes;

export const ClearButtonCombobox = () => {
  const {
    getInputProps,
    getItemProps,
    getLabelProps,
    getMenuProps,
    getToggleButtonProps,
    selectItem,
    highlightedIndex,
    isOpen,
    inputValue,
  } = useCombobox({
    initialInputValue: 'Option A',
    items,
    itemToString,
    stateReducer,
  });
  const { id: listboxId, ...listboxProps } = getMenuProps();

  const [focused, setFocused] = useState(false);

  const handleBlur = (event: FocusEvent<HTMLDivElement>) => {
    if (!event.currentTarget.contains(event.relatedTarget)) {
      setFocused(false);
    }
  };

  const onClear = () => selectItem(null);
  const showClearButton = inputValue.length > 0 && focused;

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label</Label>
          <UtilityFragment vFlexRow>
            <InputContainer
              onBlur={e => handleBlur(e)}
              onFocus={() => {
                setFocused(true);
              }}
            >
              <Input
                aria-haspopup="listbox"
                name="text-input-field-4"
                type="text"
                {...getInputProps({ 'aria-expanded': isOpen && items.length > 0, 'aria-owns': listboxId })}
              />
              {showClearButton && (
                <Button
                  aria-label="clear"
                  buttonSize="small"
                  colorScheme="tertiary"
                  iconButton
                  onClick={onClear}
                  subtle
                >
                  <VisaClearAltTiny />
                </Button>
              )}
              <Button
                aria-label="expand"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                {...getToggleButtonProps()}
              >
                {isOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />}
              </Button>
            </InputContainer>
          </UtilityFragment>
        </DropdownContainer>
      </UtilityFragment>
      <ListboxContainer>
        <Listbox id={listboxId} {...listboxProps}>
          {items.map((item, index) => (
            <ListboxItem
              className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
              key={`clear-button-combobox-${index}`}
              {...getItemProps({
                'aria-selected': inputValue === item.value,
                index,
                item,
              })}
            >
              <UtilityFragment vFlexShrink0>
                <Radio tag="span" />
              </UtilityFragment>
              {item.value}
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </Combobox>
  );
};

```

### Combobox with leading icon
- **Section**: Default Comboboxes
- **URL**: components/combobox/leading-icon-combobox
- **Tags**: docs
```tsx
import { VisaChevronDownTiny, VisaChevronUpTiny, VisaSearchLow } from '@visa/nova-icons-react';
import {
  Button,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Radio,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox } from 'downshift';

type Item = { value: string };

const items: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const stateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) =>
  // this prevents on mouse hover, the item in the list is automatic selected
  type === useCombobox.stateChangeTypes.ItemMouseMove || type === useCombobox.stateChangeTypes.MenuMouseLeave
    ? {
        ...changes, // default Downshift new state changes on item selection.
        highlightedIndex: state.highlightedIndex,
      }
    : changes;

export const LeadingIconCombobox = () => {
  const {
    getInputProps,
    getItemProps,
    getLabelProps,
    getMenuProps,
    getToggleButtonProps,
    highlightedIndex,
    inputValue,
    isOpen,
  } = useCombobox({
    items,
    itemToString,
    stateReducer,
  });
  const { id: listboxId, ...listboxProps } = getMenuProps();

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label</Label>
          <UtilityFragment vFlexRow>
            <InputContainer>
              <VisaSearchLow />
              <Input
                aria-haspopup="listbox"
                name="text-input-field-5"
                type="text"
                {...getInputProps({ 'aria-expanded': isOpen && items.length > 0, 'aria-owns': listboxId })}
              />
              <Button
                aria-label="expand"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                {...getToggleButtonProps()}
              >
                {isOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />}
              </Button>
            </InputContainer>
          </UtilityFragment>
        </DropdownContainer>
      </UtilityFragment>
      <ListboxContainer>
        <Listbox id={listboxId} {...listboxProps}>
          {items.map((item, index) => (
            <ListboxItem
              className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
              key={`clear-button-combobox-${index}`}
              {...getItemProps({
                'aria-selected': inputValue === item.value,
                index,
                item,
              })}
            >
              <UtilityFragment vFlexShrink0>
                <Radio tag="span" />
              </UtilityFragment>
              {item.value}
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </Combobox>
  );
};

```

### Combobox with error
- **Section**: Default Comboboxes
- **URL**: components/combobox/error-combobox
- **Tags**: docs
```tsx
import { VisaChevronDownTiny, VisaChevronUpTiny, VisaErrorTiny } from '@visa/nova-icons-react';
import {
  Button,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  InputMessage,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Radio,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox } from 'downshift';
import { useState } from 'react';

type Item = { value: string };

const items: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const stateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) =>
  // this prevents on mouse hover, the item in the list is automatic selected
  type === useCombobox.stateChangeTypes.ItemMouseMove || type === useCombobox.stateChangeTypes.MenuMouseLeave
    ? {
        ...changes, // default Downshift new state changes on item selection.
        highlightedIndex: state.highlightedIndex,
      }
    : changes;

export const ErrorCombobox = () => {
  const [errorState, setErrorState] = useState(false);

  const {
    getInputProps,
    getItemProps,
    getLabelProps,
    getMenuProps,
    getToggleButtonProps,
    selectItem,
    highlightedIndex,
    inputValue,
    isOpen,
    selectedItem,
  } = useCombobox({
    items,
    itemToString,
    stateReducer,
  });
  const { id: listboxId, ...listboxProps } = getMenuProps();

  return (
    <Utility vFlexCol vGap={12}>
      <Combobox>
        <DropdownContainer className="v-flex v-flex-col v-gap-4">
          <Label {...getLabelProps()}>Label (required)</Label>
          <InputContainer className="v-flex-row">
            <Input
              aria-describedby="input-error-message"
              aria-haspopup="listbox"
              aria-invalid={errorState ? 'true' : 'false'}
              name="text-input-field-6"
              type="text"
              {...getInputProps({
                'aria-expanded': isOpen && items.length > 0,
                'aria-owns': listboxId,
                onChange: () => selectItem(null),
              })}
            />
            <Button
              aria-label="expand"
              buttonSize="small"
              colorScheme="tertiary"
              iconButton
              {...getToggleButtonProps()}
            >
              {isOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />}
            </Button>
          </InputContainer>
          {errorState && !isOpen && (
            <InputMessage aria-atomic="true" aria-live="assertive" id="input-error-message" role="alert">
              <VisaErrorTiny />
              This is required text that describes the error in more detail.
            </InputMessage>
          )}
        </DropdownContainer>
        <ListboxContainer>
          <Listbox id={listboxId} {...listboxProps}>
            {items.map((item, index) => (
              <ListboxItem
                className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
                key={`error-combobox-${index}`}
                {...getItemProps({
                  'aria-selected': inputValue === item.value,
                  index,
                  item,
                })}
              >
                <UtilityFragment vFlexShrink0>
                  <Radio tag="span" />
                </UtilityFragment>
                {item.value}
              </ListboxItem>
            ))}
          </Listbox>
        </ListboxContainer>
      </Combobox>
      <Utility vFlex vGap={12}>
        <Button onClick={() => (!inputValue && !selectedItem ? setErrorState(true) : setErrorState(false))}>
          Submit
        </Button>
        <Button
          colorScheme="secondary"
          onClick={() => {
            setErrorState(false);
            selectItem(null);
          }}
        >
          Reset
        </Button>
      </Utility>
    </Utility>
  );
};

```

### Read-only combobox
- **Section**: Default Comboboxes
- **URL**: components/combobox/read-only-combobox
- **Tags**: docs
```tsx
import { VisaChevronDownTiny } from '@visa/nova-icons-react';
import { Button, Combobox, DropdownContainer, Input, InputContainer, Label, UtilityFragment } from '@visa/nova-react';
import { useCombobox } from 'downshift';

type Item = { value: string };

const items: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const ReadOnlyCombobox = () => {
  const { getInputProps, getLabelProps, getToggleButtonProps } = useCombobox({
    items: items,
    itemToString,
    initialInputValue: 'Option A',
  });

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label</Label>
          <UtilityFragment vFlexRow>
            <InputContainer>
              <Input
                aria-haspopup="listbox"
                aria-owns="combobox-listbox-example-7"
                name="text-input-field-7"
                type="text"
                {...getInputProps({ 'aria-expanded': false, readOnly: true })}
              />
              <Button
                aria-label="expand"
                buttonSize="small"
                colorScheme="tertiary"
                disabled
                iconButton
                {...getToggleButtonProps()}
              >
                <VisaChevronDownTiny />
              </Button>
            </InputContainer>
          </UtilityFragment>
        </DropdownContainer>
      </UtilityFragment>
    </Combobox>
  );
};

```

### Disabled combobox
- **Section**: Default Comboboxes
- **URL**: components/combobox/disabled-combobox
- **Tags**: docs
```tsx
import { VisaChevronDownTiny } from '@visa/nova-icons-react';
import {
  Button,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Radio,
  UtilityFragment,
} from '@visa/nova-react';
import { useCombobox } from 'downshift';

type Item = { value: string };

const items: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const DisabledCombobox = () => {
  const { getInputProps, getItemProps, getLabelProps, getMenuProps, getToggleButtonProps, inputValue, isOpen } =
    useCombobox({
      items: items,
      itemToString,
      initialInputValue: 'Option A',
    });
  const { id: listboxId, ...listboxProps } = getMenuProps();

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label</Label>
          <UtilityFragment vFlexRow>
            <InputContainer>
              <Input
                aria-haspopup="listbox"
                disabled
                name="text-input-field-8"
                type="text"
                {...getInputProps({ 'aria-expanded': isOpen, 'aria-owns': listboxId })}
              />
              <Button
                aria-label="expand"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                {...getToggleButtonProps()}
              >
                <VisaChevronDownTiny />
              </Button>
            </InputContainer>
          </UtilityFragment>
        </DropdownContainer>
      </UtilityFragment>
      <ListboxContainer>
        <Listbox id={listboxId} {...listboxProps}>
          {items.map((item, index) => (
            <ListboxItem
              key={`disabled-example-${index}`}
              {...getItemProps({
                'aria-selected': inputValue === item.value,
                index,
                item,
              })}
            >
              <UtilityFragment vFlexShrink0>
                <Radio tag="span" />
              </UtilityFragment>
              {item.value}
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </Combobox>
  );
};

```

### Combobox with disabled option
- **Section**: Default Comboboxes
- **URL**: components/combobox/item-disabled-combobox
- **Tags**: docs
```tsx
import { VisaChevronDownTiny } from '@visa/nova-icons-react';
import {
  Button,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Radio,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox } from 'downshift';

type Item = { value: string };

const items: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const stateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) =>
  // this prevents on mouse hover, the item in the list is automatic selected
  type === useCombobox.stateChangeTypes.ItemMouseMove || type === useCombobox.stateChangeTypes.MenuMouseLeave
    ? {
        ...changes, // default Downshift new state changes on item selection.
        highlightedIndex: state.highlightedIndex,
      }
    : changes;

export const ItemDisabledCombobox = () => {
  const {
    getInputProps,
    getItemProps,
    getLabelProps,
    getMenuProps,
    getToggleButtonProps,
    highlightedIndex,
    inputValue,
    isOpen,
  } = useCombobox({
    items: items,
    itemToString,
    stateReducer,
    isItemDisabled: item => item.value === 'Option C', // This is just to mock the third option to be disabled
  });
  const { id: listboxId, ...listboxProps } = getMenuProps();

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label</Label>
          <UtilityFragment vFlexRow>
            <InputContainer>
              <Input
                aria-haspopup="listbox"
                name="text-input-field-9"
                type="text"
                {...getInputProps({ 'aria-expanded': isOpen, 'aria-owns': listboxId })}
              />
              <Button
                aria-label="expand"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                {...getToggleButtonProps()}
              >
                <VisaChevronDownTiny />
              </Button>
            </InputContainer>
          </UtilityFragment>
        </DropdownContainer>
      </UtilityFragment>
      <ListboxContainer>
        <Listbox id={listboxId} {...listboxProps}>
          {items.map((item, index) => (
            <ListboxItem
              className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
              disabled={item.value === 'Option C'} // This is just to mock the third option to be disabled
              key={`item-disabled-example-${index}`}
              {...getItemProps({
                'aria-selected': inputValue === item.value,
                index,
                item,
              })}
            >
              <UtilityFragment vFlexShrink0>
                <Radio tag="span" />
              </UtilityFragment>
              {item.value}
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </Combobox>
  );
};

```

### Combobox without dropdown chevron
- **Section**: Default Comboboxes
- **URL**: components/combobox/no-icon-combobox
- **Tags**: docs
```tsx
import {
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Radio,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox } from 'downshift';

type Item = { value: string };

const items: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const stateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) =>
  // this prevents on mouse hover, the item in the list is automatic selected
  type === useCombobox.stateChangeTypes.ItemMouseMove || type === useCombobox.stateChangeTypes.MenuMouseLeave
    ? {
        ...changes, // default Downshift new state changes on item selection.
        highlightedIndex: state.highlightedIndex,
      }
    : changes;

export const NoIconCombobox = () => {
  const { getInputProps, getItemProps, getLabelProps, getMenuProps, highlightedIndex, inputValue, isOpen } =
    useCombobox({
      items: items,
      itemToString,
      stateReducer,
    });
  const { id: listboxId, ...listboxProps } = getMenuProps();

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label</Label>
          <UtilityFragment vFlexRow>
            <InputContainer>
              <Input
                aria-haspopup="listbox"
                name="text-input-field-10"
                type="text"
                {...getInputProps({ 'aria-expanded': isOpen, 'aria-owns': listboxId })}
              />
            </InputContainer>
          </UtilityFragment>
        </DropdownContainer>
      </UtilityFragment>
      <ListboxContainer>
        <Listbox id={listboxId} {...listboxProps}>
          {items.map((item, index) => (
            <ListboxItem
              className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
              key={`no-icon-example-${index}`}
              {...getItemProps({
                'aria-selected': inputValue === item.value,
                index,
                item,
              })}
            >
              <UtilityFragment vFlexShrink0>
                <Radio tag="span" />
              </UtilityFragment>
              {item.value}
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </Combobox>
  );
};

```

### Combobox with filterable menu and manual selection
- **Section**: Combobox behaviors
- **URL**: components/combobox/autocomplete-with-manual-selection-combobox
- **Tags**: docs
```tsx
import { VisaChevronDownTiny, VisaChevronUpTiny } from '@visa/nova-icons-react';
import {
  Button,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Radio,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox } from 'downshift';
import { useState } from 'react';

type Item = { value: string };

const defaultItems: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const filter = (item: Item, inputValue: string = '') =>
  item.value.toLowerCase().includes(inputValue!.toLowerCase());

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const stateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) =>
  // this prevents on mouse hover, the item in the list is automatic selected
  type === useCombobox.stateChangeTypes.ItemMouseMove || type === useCombobox.stateChangeTypes.MenuMouseLeave
    ? {
        ...changes, // default Downshift new state changes on item selection.
        highlightedIndex: state.highlightedIndex,
      }
    : changes;

export const AutocompleteWithManualSelectionCombobox = () => {
  const [items, setItems] = useState(defaultItems);
  const {
    getInputProps,
    getItemProps,
    getLabelProps,
    getMenuProps,
    getToggleButtonProps,
    highlightedIndex,
    inputValue,
    isOpen,
  } = useCombobox({
    items,
    itemToString,
    onInputValueChange: ({ inputValue }) => {
      setItems(defaultItems.filter(item => filter(item, inputValue)));
    },
    stateReducer,
  });

  const { id: listboxId, ...listboxProps } = getMenuProps();

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label</Label>
          <UtilityFragment vFlexRow>
            <InputContainer>
              <Input
                aria-haspopup="listbox"
                name="text-input-field-12"
                type="text"
                {...getInputProps({
                  'aria-expanded': isOpen && items.length > 0,
                  'aria-owns': listboxId
                })}
              />
              <Button
                aria-label="expand"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                {...getToggleButtonProps()}
              >
                {isOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />}
              </Button>
            </InputContainer>
          </UtilityFragment>
        </DropdownContainer>
      </UtilityFragment>
      <ListboxContainer>
        <Listbox id={listboxId} {...listboxProps}>
          {items.length > 0 ? (
            items.map((item, index) => (
              <ListboxItem
                className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
                key={`manual-autocomplete-combobox-${index}`}
                {...getItemProps({
                  'aria-selected': inputValue === item.value,
                  index,
                  item,
                })}
              >
                <UtilityFragment vFlexShrink0>
                  <Radio tag="span" />
                </UtilityFragment>
                {item.value}
              </ListboxItem>
            ))
          ) : (
            <UtilityFragment vFlex vJustifyContent="center" vPaddingVertical={8}>
              <li>No results found.</li>
            </UtilityFragment>
          )}
        </Listbox>
      </ListboxContainer>
    </Combobox>
  );
};

```

### Combobox with filterable menu and automatic selection
- **Section**: Combobox behaviors
- **URL**: components/combobox/autocomplete-with-automatic-selection-combobox
- **Tags**: docs
```tsx
import { VisaChevronDownTiny, VisaChevronUpTiny } from '@visa/nova-icons-react';
import {
  Button,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Radio,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox } from 'downshift';
import { useState } from 'react';

type Item = { value: string };

const defaultItems: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const filter = (item: Item, inputValue: string = '') =>
  item.value.toLowerCase().includes(inputValue.toLowerCase());

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const stateReducer = <TItemType,>(
  state: UseComboboxState<TItemType>,
  { type, changes }: UseComboboxStateChangeOptions<TItemType>
) =>
  // this prevents on mouse hover, the item in the list is automatic selected
  type === useCombobox.stateChangeTypes.ItemMouseMove || type === useCombobox.stateChangeTypes.MenuMouseLeave
    ? {
        ...changes, // default Downshift new state changes on item selection.
        highlightedIndex: state.highlightedIndex,
      }
    : changes;

export const AutocompleteWithAutomaticSelectionCombobox = () => {
  const [items, setItems] = useState(defaultItems);
  const {
    isOpen,
    getToggleButtonProps,
    getLabelProps,
    getInputProps,
    getMenuProps,
    getItemProps,
    setHighlightedIndex,
  } = useCombobox({
    items: items,
    itemToString,
    onInputValueChange: ({ inputValue }) => {
      setItems(defaultItems.filter(item => filter(item, inputValue)));
      if (inputValue) setHighlightedIndex(0);
    },
    stateReducer,
  });

  const { id: listboxId, ...listboxProps } = getMenuProps();

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label</Label>
          <UtilityFragment vFlexRow>
            <InputContainer>
              <Input
                aria-haspopup="listbox"
                name="text-input-field-11"
                type="text"
                {...getInputProps({
                  'aria-autocomplete': 'list',
                  'aria-expanded': isOpen && items.length > 0,
                  'aria-owns': listboxId,
                })}
              />
              <Button
                aria-label="expand"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                {...getToggleButtonProps()}
              >
                {isOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />}
              </Button>
            </InputContainer>
          </UtilityFragment>
        </DropdownContainer>
      </UtilityFragment>
      <ListboxContainer>
        <Listbox id={listboxId} {...listboxProps}>
          {items.length > 0 ? (
            items.map((item, index) => (
              <ListboxItem
                key={`auto-autocomplete-combobox-${index}`}
                {...getItemProps({
                  index,
                  item,
                })}
              >
                <UtilityFragment vFlexShrink0>
                  <Radio tag="span" />
                </UtilityFragment>
                {item.value}
              </ListboxItem>
            ))
          ) : (
            <UtilityFragment vFlex vJustifyContent="center" vPaddingVertical={8}>
              <li>No results found.</li>
            </UtilityFragment>
          )}
        </Listbox>
      </ListboxContainer>
    </Combobox>
  );
};

```

## Property Sections
### Combobox
- **Selector**: <Combobox />
- **Description**: Dropdown menu enabling users to enter text or select items from a list.

### DropdownMenu
- **Selector**: <DropdownMenu />
- **Description**: Interactive element enabling users to select a single option from a list.

### dropdown-menu
- **Selector**: <DropdownMenu />
- **Description**: 

## Properties
### ref
- **Section**: Combobox
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Combobox
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of the component

### ref
- **Section**: DropdownMenu
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: DropdownMenu
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Scroll

