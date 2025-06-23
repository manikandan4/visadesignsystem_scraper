# multiselect

## Metadata
- **Version**: 0.0.1
- **Description**: Control that allows users to select multiple options from a dropdown menu.
- **Category**: components

## Example Sections
1. **Default multiselects**
   - Description: 
2. **Multiselect Behaviors**
   - Description: 

## Examples
### Default multiselect
- **Section**: Default multiselects
- **URL**: components/multiselect/default-multiselect
- **Tags**: docs
```tsx
import { VisaChevronDownTiny, VisaChevronUpTiny, VisaClearAltTiny } from '@visa/nova-icons-react';
import {
  Button,
  Checkbox,
  Chip,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox, useMultipleSelection } from 'downshift';
import { useState } from 'react';

type Item = { value: string };

const id = 'default-multiselect';
const multiselectItems: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const comboboxStateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) => {
  switch (type) {
    case useCombobox.stateChangeTypes.InputClick:
      return {
        // don't open the menu just because the input was clicked
        // instead, wait for an keystroke or a toggle button click
        ...state,
      };
    case useCombobox.stateChangeTypes.InputChange:
      return {
        ...changes,
        // don't update the highlighted index
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.ItemMouseMove:
    case useCombobox.stateChangeTypes.MenuMouseLeave:
      return {
        ...changes,
        // don't change the focused item just because the mouse moved
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.InputKeyDownEnter:
    case useCombobox.stateChangeTypes.ItemClick:
      return {
        ...changes,
        isOpen: true, // keep the menu open on item select or Enter press
        // and if we're selecting an item, maintain the same highlightedIndex
        ...(changes.selectedItem && { highlightedIndex: state.highlightedIndex }),
      };
    default:
      return changes;
  }
};

export const DefaultMultiselect = () => {
  const [inputValue, setInputValue] = useState('');
  const [selectedItems, setSelectedItems] = useState<Item[]>([]);
  const items = multiselectItems;

  const { getDropdownProps, removeSelectedItem } = useMultipleSelection({
    selectedItems,
    onStateChange({ selectedItems: newSelectedItems, type }) {
      if (
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownDelete ||
        type === useMultipleSelection.stateChangeTypes.DropdownKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.FunctionRemoveSelectedItem
      ) {
        setSelectedItems(newSelectedItems!);
      }
    },
  });
  const {
    getToggleButtonProps,
    getLabelProps,
    getMenuProps,
    getInputProps,
    getItemProps,
    highlightedIndex,
    isOpen,
    setHighlightedIndex,
  } = useCombobox({
    items,
    itemToString,
    inputValue,
    stateReducer: comboboxStateReducer,
    onStateChange({ inputValue: newInputValue, type, selectedItem }) {
      if (type === useCombobox.stateChangeTypes.InputChange) {
        setInputValue(newInputValue!);
      }
      if (type === useCombobox.stateChangeTypes.ItemClick && !!selectedItem) {
        // make sure the highlighted index is on the item that was just clicked
        setHighlightedIndex(items.indexOf(selectedItem));
      }
    },
  });

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label (required)</Label>
          <UtilityFragment vPaddingVertical={3} vPaddingLeft={3} vPaddingRight={6}>
            <InputContainer>
              <Utility vFlex vFlexGrow vFlexShrink vFlexWrap vGap={2}>
                {selectedItems.map((item, index) => (
                  <UtilityFragment vFlexShrink0 key={`selected-item-${index}`}>
                    <Chip chipSize="compact">
                      <Label>{item.value}</Label>
                      <Button
                        aria-label={`Remove ${item.value}`}
                        colorScheme="tertiary"
                        iconButton
                        onClick={() => removeSelectedItem(item)}
                        subtle
                      >
                        <VisaClearAltTiny />
                      </Button>
                    </Chip>
                  </UtilityFragment>
                ))}
                <UtilityFragment vFlexShrink style={{ flexBasis: '50px' }}>
                  <Input
                    name={id}
                    {...getInputProps(
                      getDropdownProps({
                        onKeyDown: e => {
                          if (e.key === 'Enter') {
                            if (highlightedIndex !== -1 && isOpen) {
                              const selectedItem = items[highlightedIndex];
                              if (selectedItems.includes(selectedItem)) {
                                removeSelectedItem(selectedItem);
                              } else {
                                setSelectedItems([...selectedItems, selectedItem]);
                                setInputValue('');
                              }
                            }
                          }
                        },
                      })
                    )}
                  />
                </UtilityFragment>
              </Utility>
              <Button
                aria-haspopup="listbox"
                aria-label={`${id}-toggle-button`}
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
        <UtilityFragment vFlex>
          <Listbox {...getMenuProps()}>
            {items.map((item, index) => (
              <ListboxItem<HTMLLIElement>
                key={`${id}-example-${index}`}
                className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
                {...getItemProps({
                  item,
                  index,
                  'aria-selected': selectedItems.includes(item),
                  onClick: () => {
                    if (selectedItems.includes(item)) {
                      removeSelectedItem(item);
                    } else {
                      setSelectedItems([...selectedItems, item]);
                      setInputValue('');
                    }
                  },
                })}
              >
                <Checkbox tag="span" />
                {item.value}
              </ListboxItem>
            ))}
          </Listbox>
        </UtilityFragment>
      </ListboxContainer>
    </Combobox>
  );
};

```

### Multiselect with inline message
- **Section**: Default multiselects
- **URL**: components/multiselect/multiselect-with-inline-message
- **Tags**: docs
```tsx
import { VisaChevronDownTiny, VisaChevronUpTiny, VisaClearAltTiny } from '@visa/nova-icons-react';
import {
  Button,
  Checkbox,
  Chip,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  InputMessage,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox, useMultipleSelection } from 'downshift';
import { useState } from 'react';

type Item = { value: string };

const id = 'multiselect-with-inline-message';
const multiselectItems: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const comboboxStateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) => {
  switch (type) {
    case useCombobox.stateChangeTypes.InputClick:
      return {
        // don't open the menu just because the input was clicked
        // instead, wait for an keystroke or a toggle button click
        ...state,
      };
    case useCombobox.stateChangeTypes.InputChange:
      return {
        ...changes,
        // don't update the highlighted index
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.ItemMouseMove:
    case useCombobox.stateChangeTypes.MenuMouseLeave:
      return {
        ...changes,
        // don't change the focused item just because the mouse moved
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.InputKeyDownEnter:
    case useCombobox.stateChangeTypes.ItemClick:
      return {
        ...changes,
        isOpen: true, // keep the menu open on item select or Enter press
        // and if we're selecting an item, maintain the same highlightedIndex
        ...(changes.selectedItem && { highlightedIndex: state.highlightedIndex }),
      };
    default:
      return changes;
  }
};

export const MultiselectWithInlineMessage = () => {
  const [inputValue, setInputValue] = useState('');
  const [selectedItems, setSelectedItems] = useState<Item[]>([]);
  const items = multiselectItems;

  const { getDropdownProps, removeSelectedItem } = useMultipleSelection({
    selectedItems,
    onStateChange({ selectedItems: newSelectedItems, type }) {
      if (
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownDelete ||
        type === useMultipleSelection.stateChangeTypes.DropdownKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.FunctionRemoveSelectedItem
      ) {
        setSelectedItems(newSelectedItems!);
      }
    },
  });
  const {
    getToggleButtonProps,
    getLabelProps,
    getMenuProps,
    getInputProps,
    getItemProps,
    highlightedIndex,
    isOpen,
    setHighlightedIndex,
  } = useCombobox({
    items,
    itemToString,
    inputValue,
    stateReducer: comboboxStateReducer,
    onStateChange({ inputValue: newInputValue, type, selectedItem }) {
      if (type === useCombobox.stateChangeTypes.InputChange) {
        setInputValue(newInputValue!);
      }
      if (type === useCombobox.stateChangeTypes.ItemClick && !!selectedItem) {
        // make sure the highlighted index is on the item that was just clicked
        setHighlightedIndex(items.indexOf(selectedItem));
      }
    },
  });

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label (required)</Label>
          <UtilityFragment vPaddingVertical={3} vPaddingLeft={3} vPaddingRight={6}>
            <InputContainer>
              <Utility vFlex vFlexGrow vFlexShrink vFlexWrap vGap={2}>
                {selectedItems.map((item, index) => (
                  <UtilityFragment vFlexShrink0 key={`selected-item-${index}`}>
                    <Chip chipSize="compact">
                      <Label>{item.value}</Label>
                      <Button
                        aria-label={`Remove ${item.value}`}
                        colorScheme="tertiary"
                        iconButton
                        onClick={() => removeSelectedItem(item)}
                        subtle
                      >
                        <VisaClearAltTiny />
                      </Button>
                    </Chip>
                  </UtilityFragment>
                ))}
                <UtilityFragment vFlexShrink style={{ flexBasis: '50px' }}>
                  <Input
                    name={id}
                    {...getInputProps(
                      getDropdownProps({
                        onKeyDown: e => {
                          if (e.key === 'Enter') {
                            if (highlightedIndex !== -1 && isOpen) {
                              const selectedItem = items[highlightedIndex];
                              if (selectedItems.includes(selectedItem)) {
                                removeSelectedItem(selectedItem);
                              } else {
                                setSelectedItems([...selectedItems, selectedItem]);
                                setInputValue('');
                              }
                            }
                          }
                        },
                      })
                    )}
                  />
                </UtilityFragment>
              </Utility>
              <Button
                aria-haspopup="listbox"
                aria-label={`${id}-toggle-button`}
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                {...getToggleButtonProps()}
              >
                {isOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />}
              </Button>
            </InputContainer>
          </UtilityFragment>
          <UtilityFragment vHide={isOpen}>
            <InputMessage id={`${id}-message`}>
              This is optional text that describes the label in more detail.
            </InputMessage>
          </UtilityFragment>
        </DropdownContainer>
      </UtilityFragment>
      <ListboxContainer>
        <UtilityFragment vFlex>
          <Listbox {...getMenuProps()}>
            {items.map((item, index) => (
              <ListboxItem<HTMLLIElement>
                key={`${id}-example-${index}`}
                className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
                {...getItemProps({
                  item,
                  index,
                  'aria-selected': selectedItems.includes(item),
                  onClick: () => {
                    if (selectedItems.includes(item)) {
                      removeSelectedItem(item);
                    } else {
                      setSelectedItems([...selectedItems, item]);
                      setInputValue('');
                    }
                  },
                })}
              >
                <Checkbox tag="span" />
                {item.value}
              </ListboxItem>
            ))}
          </Listbox>
        </UtilityFragment>
      </ListboxContainer>
    </Combobox>
  );
};

```

### Multiselect with error
- **Section**: Default multiselects
- **URL**: components/multiselect/multiselect-with-error
- **Tags**: docs
```tsx
import { VisaChevronDownTiny, VisaChevronUpTiny, VisaClearAltTiny, VisaErrorTiny } from '@visa/nova-icons-react';
import {
  Button,
  Checkbox,
  Chip,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  InputMessage,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox, useMultipleSelection } from 'downshift';
import { useRef, useState } from 'react';

type Item = { value: string };

const id = 'multiselect-with-error';
const multiselectItems: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const comboboxStateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) => {
  switch (type) {
    case useCombobox.stateChangeTypes.InputClick:
      return {
        // don't open the menu just because the input was clicked
        // instead, wait for an keystroke or a toggle button click
        ...state,
      };
    case useCombobox.stateChangeTypes.InputChange:
      return {
        ...changes,
        // don't update the highlighted index
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.ItemMouseMove:
    case useCombobox.stateChangeTypes.MenuMouseLeave:
      return {
        ...changes,
        // don't change the focused item just because the mouse moved
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.InputKeyDownEnter:
    case useCombobox.stateChangeTypes.ItemClick:
      return {
        ...changes,
        isOpen: true, // keep the menu open on item select or Enter press
        // and if we're selecting an item, maintain the same highlightedIndex
        ...(changes.selectedItem && { highlightedIndex: state.highlightedIndex }),
      };
    default:
      return changes;
  }
};

export const MultiselectWithError = () => {
  const [inputValue, setInputValue] = useState('');
  const [selectedItems, setSelectedItems] = useState<Item[]>([]);
  const items = multiselectItems;

  const { getDropdownProps, removeSelectedItem, reset } = useMultipleSelection({
    selectedItems,
    onStateChange({ selectedItems: newSelectedItems, type }) {
      if (
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownDelete ||
        type === useMultipleSelection.stateChangeTypes.DropdownKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.FunctionRemoveSelectedItem
      ) {
        setSelectedItems(newSelectedItems!);
      }
      if (type === useMultipleSelection.stateChangeTypes.FunctionReset) {
        setSelectedItems([]);
        setInputValue('');
        setHasError(false);
      }
    },
  });
  const {
    getToggleButtonProps,
    getLabelProps,
    getMenuProps,
    getInputProps,
    getItemProps,
    highlightedIndex,
    isOpen,
    setHighlightedIndex,
  } = useCombobox({
    items,
    itemToString,
    inputValue,
    stateReducer: comboboxStateReducer,
    onStateChange({ inputValue: newInputValue, type, selectedItem }) {
      if (type === useCombobox.stateChangeTypes.InputChange) {
        setInputValue(newInputValue!);
      }
      if (type === useCombobox.stateChangeTypes.ItemClick && !!selectedItem) {
        // make sure the highlighted index is on the item that was just clicked
        setHighlightedIndex(items.indexOf(selectedItem));
      }
    },
  });

  const [hasError, setHasError] = useState(false);
  const dropdownRef = useRef<HTMLInputElement | null>(null);

  const handleSubmit = () => {
    // Customize this for your own validation needs
    if (!selectedItems.length) {
      setHasError(true);
    }

    // Focus on the field with the error
    if (dropdownRef.current) {
      dropdownRef.current.focus();
    }
  };
  const handleReset = () => {
    reset();
  };

  return (
    <>
      <Combobox>
        <UtilityFragment vFlex vFlexCol vGap={4}>
          <DropdownContainer>
            <Label {...getLabelProps()}>Label (required)</Label>
            <UtilityFragment vPaddingVertical={3} vPaddingLeft={3} vPaddingRight={6}>
              <InputContainer>
                <Utility vFlex vFlexGrow vFlexShrink vFlexWrap vGap={2}>
                  {selectedItems.map((item, index) => (
                    <UtilityFragment vFlexShrink0 key={`selected-item-${index}`}>
                      <Chip chipSize="compact">
                        <Label>{item.value}</Label>
                        <Button
                          aria-label={`Remove ${item.value}`}
                          colorScheme="tertiary"
                          iconButton
                          onClick={() => removeSelectedItem(item)}
                          subtle
                        >
                          <VisaClearAltTiny />
                        </Button>
                      </Chip>
                    </UtilityFragment>
                  ))}
                  <UtilityFragment vFlexShrink style={{ flexBasis: '50px' }}>
                    <Input
                      name={id}
                      aria-invalid={hasError}
                      {...getInputProps(
                        getDropdownProps({
                          ref: dropdownRef,
                          onKeyDown: e => {
                            if (e.key === 'Enter') {
                              if (highlightedIndex !== -1 && isOpen) {
                                const selectedItem = items[highlightedIndex];
                                if (selectedItems.includes(selectedItem)) {
                                  removeSelectedItem(selectedItem);
                                } else {
                                  setSelectedItems([...selectedItems, selectedItem]);
                                  setInputValue('');
                                  setHasError(false);
                                }
                              }
                            }
                          },
                        })
                      )}
                    />
                  </UtilityFragment>
                </Utility>
                <Button
                  aria-haspopup="listbox"
                  aria-label={`${id}-toggle-button`}
                  buttonSize="small"
                  colorScheme="tertiary"
                  iconButton
                  {...getToggleButtonProps()}
                >
                  {isOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />}
                </Button>
              </InputContainer>
            </UtilityFragment>
            {hasError && (
              <InputMessage aria-atomic="true" aria-live="assertive" id={`${id}-message`} role="alert">
                <VisaErrorTiny />
                This is required text that describes the error in more detail.
              </InputMessage>
            )}
          </DropdownContainer>
        </UtilityFragment>
        <ListboxContainer>
          <UtilityFragment vFlex>
            <Listbox {...getMenuProps()}>
              {items.map((item, index) => (
                <ListboxItem<HTMLLIElement>
                  key={`${id}-example-${index}`}
                  className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
                  {...getItemProps({
                    item,
                    index,
                    'aria-selected': selectedItems.includes(item),
                    onClick: () => {
                      if (selectedItems.includes(item)) {
                        removeSelectedItem(item);
                      } else {
                        setSelectedItems([...selectedItems, item]);
                        setInputValue('');
                        setHasError(false);
                      }
                    },
                  })}
                >
                  <Checkbox tag="span" />
                  {item.value}
                </ListboxItem>
              ))}
            </Listbox>
          </UtilityFragment>
        </ListboxContainer>
      </Combobox>
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

### Multiselect with disabled option
- **Section**: Default multiselects
- **URL**: components/multiselect/multiselect-with-disabled-option
- **Tags**: docs
```tsx
import { VisaChevronDownTiny, VisaChevronUpTiny, VisaClearAltTiny } from '@visa/nova-icons-react';
import {
  Button,
  Checkbox,
  Chip,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox, useMultipleSelection } from 'downshift';
import { useState } from 'react';

type Item = { value: string; disabled?: boolean };

const id = 'multiselect-with-disabled-option';
const multiselectItems: Item[] = [
  { value: 'Option A' },
  { value: 'Option B', disabled: true },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const comboboxStateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) => {
  switch (type) {
    case useCombobox.stateChangeTypes.InputClick:
      return {
        // don't open the menu just because the input was clicked
        // instead, wait for an keystroke or a toggle button click
        ...state,
      };
    case useCombobox.stateChangeTypes.InputChange:
      return {
        ...changes,
        // don't update the highlighted index
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.ItemMouseMove:
    case useCombobox.stateChangeTypes.MenuMouseLeave:
      return {
        ...changes,
        // don't change the focused item just because the mouse moved
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.InputKeyDownEnter:
    case useCombobox.stateChangeTypes.ItemClick:
      return {
        ...changes,
        isOpen: true, // keep the menu open on item select or Enter press
        // and if we're selecting an item, maintain the same highlightedIndex
        ...(changes.selectedItem && { highlightedIndex: state.highlightedIndex }),
      };
    default:
      return changes;
  }
};

export const MultiselectWithDisabledOption = () => {
  const [inputValue, setInputValue] = useState('');
  const [selectedItems, setSelectedItems] = useState<Item[]>([]);
  const items = multiselectItems;

  const { getDropdownProps, removeSelectedItem } = useMultipleSelection({
    selectedItems,
    onStateChange({ selectedItems: newSelectedItems, type }) {
      if (
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownDelete ||
        type === useMultipleSelection.stateChangeTypes.DropdownKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.FunctionRemoveSelectedItem
      ) {
        setSelectedItems(newSelectedItems!);
      }
    },
  });
  const {
    getToggleButtonProps,
    getLabelProps,
    getMenuProps,
    getInputProps,
    getItemProps,
    highlightedIndex,
    isOpen,
    setHighlightedIndex,
  } = useCombobox({
    items,
    itemToString,
    inputValue,
    stateReducer: comboboxStateReducer,
    isItemDisabled: item => !!item.disabled,
    onStateChange({ inputValue: newInputValue, type, selectedItem }) {
      if (type === useCombobox.stateChangeTypes.InputChange) {
        setInputValue(newInputValue!);
      }
      if (type === useCombobox.stateChangeTypes.ItemClick && !!selectedItem) {
        // make sure the highlighted index is on the item that was just clicked
        setHighlightedIndex(items.indexOf(selectedItem));
      }
    },
  });

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label (required)</Label>
          <UtilityFragment vPaddingVertical={3} vPaddingLeft={3} vPaddingRight={6}>
            <InputContainer>
              <Utility vFlex vFlexGrow vFlexShrink vFlexWrap vGap={2}>
                {selectedItems.map((item, index) => (
                  <UtilityFragment vFlexShrink0 key={`selected-item-${index}`}>
                    <Chip chipSize="compact">
                      <Label>{item.value}</Label>
                      <Button
                        aria-label={`Remove ${item.value}`}
                        colorScheme="tertiary"
                        iconButton
                        onClick={() => removeSelectedItem(item)}
                        subtle
                      >
                        <VisaClearAltTiny />
                      </Button>
                    </Chip>
                  </UtilityFragment>
                ))}
                <UtilityFragment vFlexShrink style={{ flexBasis: '50px' }}>
                  <Input
                    name={id}
                    {...getInputProps(
                      getDropdownProps({
                        onKeyDown: e => {
                          if (e.key === 'Enter') {
                            if (highlightedIndex !== -1 && isOpen) {
                              const selectedItem = items[highlightedIndex];
                              if (selectedItems.includes(selectedItem)) {
                                removeSelectedItem(selectedItem);
                              } else {
                                setSelectedItems([...selectedItems, selectedItem]);
                                setInputValue('');
                              }
                            }
                          }
                        },
                      })
                    )}
                  />
                </UtilityFragment>
              </Utility>
              <Button
                aria-haspopup="listbox"
                aria-label={`${id}-toggle-button`}
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
        <UtilityFragment vFlex>
          <Listbox {...getMenuProps()}>
            {items.map((item, index) => (
              <ListboxItem<HTMLLIElement>
                key={`${id}-example-${index}`}
                className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
                {...getItemProps({
                  item,
                  index,
                  'aria-selected': selectedItems.includes(item),
                  'aria-disabled': item.disabled,
                  onClick: () => {
                    if (selectedItems.includes(item)) {
                      removeSelectedItem(item);
                    } else {
                      setSelectedItems([...selectedItems, item]);
                      setInputValue('');
                    }
                  },
                })}
              >
                <Checkbox tag="span" />
                {item.value}
              </ListboxItem>
            ))}
          </Listbox>
        </UtilityFragment>
      </ListboxContainer>
    </Combobox>
  );
};

```

### Disabled multiselect
- **Section**: Default multiselects
- **URL**: components/multiselect/disabled-multiselect
- **Tags**: docs
```tsx
import { VisaChevronDownTiny, VisaChevronUpTiny, VisaClearAltTiny } from '@visa/nova-icons-react';
import {
  Button,
  Checkbox,
  Chip,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox, useMultipleSelection } from 'downshift';
import { useState } from 'react';

type Item = { value: string };

const id = 'disabled-multiselect';
const multiselectItems: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const comboboxStateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) => {
  switch (type) {
    case useCombobox.stateChangeTypes.InputClick:
      return {
        // don't open the menu just because the input was clicked
        // instead, wait for an keystroke or a toggle button click
        ...state,
      };
    case useCombobox.stateChangeTypes.InputChange:
      return {
        ...changes,
        // don't update the highlighted index
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.ItemMouseMove:
    case useCombobox.stateChangeTypes.MenuMouseLeave:
      return {
        ...changes,
        // don't change the focused item just because the mouse moved
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.InputKeyDownEnter:
    case useCombobox.stateChangeTypes.ItemClick:
      return {
        ...changes,
        isOpen: true, // keep the menu open on item select or Enter press
        // and if we're selecting an item, maintain the same highlightedIndex
        ...(changes.selectedItem && { highlightedIndex: state.highlightedIndex }),
      };
    default:
      return changes;
  }
};

export const DisabledMultiselect = () => {
  const [inputValue, setInputValue] = useState('');
  const [selectedItems, setSelectedItems] = useState<Item[]>([]);
  const [isDisabled, setIsDisabled] = useState(true);

  const items = multiselectItems;

  const { getDropdownProps, removeSelectedItem } = useMultipleSelection({
    selectedItems,
    onStateChange({ selectedItems: newSelectedItems, type }) {
      if (
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownDelete ||
        type === useMultipleSelection.stateChangeTypes.DropdownKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.FunctionRemoveSelectedItem
      ) {
        setSelectedItems(newSelectedItems!);
      }
    },
  });
  const {
    getToggleButtonProps,
    getLabelProps,
    getMenuProps,
    getInputProps,
    getItemProps,
    highlightedIndex,
    isOpen,
    setHighlightedIndex,
  } = useCombobox({
    items,
    itemToString,
    inputValue,
    stateReducer: comboboxStateReducer,
    onStateChange({ inputValue: newInputValue, type, selectedItem }) {
      if (type === useCombobox.stateChangeTypes.InputChange) {
        setInputValue(newInputValue!);
      }
      if (type === useCombobox.stateChangeTypes.ItemClick && !!selectedItem) {
        // make sure the highlighted index is on the item that was just clicked
        setHighlightedIndex(items.indexOf(selectedItem));
      }
    },
  });

  return (
    <>
      <Combobox>
        <UtilityFragment vFlex vFlexCol vGap={4}>
          <DropdownContainer>
            <Label {...getLabelProps()}>Label (required)</Label>
            <UtilityFragment vPaddingVertical={3} vPaddingLeft={3} vPaddingRight={6}>
              <InputContainer>
                <Utility vFlex vFlexGrow vFlexShrink vFlexWrap vGap={2}>
                  {selectedItems.map((item, index) => (
                    <UtilityFragment vFlexShrink0 key={`selected-item-${index}`}>
                      <Chip chipSize="compact">
                        <Label>{item.value}</Label>
                        <Button
                          aria-label={`Remove ${item.value}`}
                          colorScheme="tertiary"
                          iconButton
                          onClick={() => removeSelectedItem(item)}
                          subtle
                          disabled={isDisabled}
                        >
                          <VisaClearAltTiny />
                        </Button>
                      </Chip>
                    </UtilityFragment>
                  ))}
                  <UtilityFragment vFlexShrink style={{ flexBasis: '50px' }}>
                    <Input
                      name={id}
                      disabled={isDisabled}
                      {...getInputProps(
                        getDropdownProps({
                          onKeyDown: e => {
                            if (e.key === 'Enter') {
                              if (highlightedIndex !== -1 && isOpen) {
                                const selectedItem = items[highlightedIndex];
                                if (selectedItems.includes(selectedItem)) {
                                  removeSelectedItem(selectedItem);
                                } else {
                                  setSelectedItems([...selectedItems, selectedItem]);
                                  setInputValue('');
                                }
                              }
                            }
                          },
                        })
                      )}
                    />
                  </UtilityFragment>
                </Utility>
                <Button
                  aria-haspopup="listbox"
                  aria-label={`${id}-toggle-button`}
                  buttonSize="small"
                  colorScheme="tertiary"
                  iconButton
                  disabled={isDisabled}
                  {...getToggleButtonProps()}
                >
                  {isOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />}
                </Button>
              </InputContainer>
            </UtilityFragment>
          </DropdownContainer>
        </UtilityFragment>
        <ListboxContainer>
          <UtilityFragment vFlex>
            <Listbox {...getMenuProps()}>
              {items.map((item, index) => (
                <ListboxItem<HTMLLIElement>
                  key={`${id}-example-${index}`}
                  className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
                  {...getItemProps({
                    item,
                    index,
                    'aria-selected': selectedItems.includes(item),
                    onClick: () => {
                      if (selectedItems.includes(item)) {
                        removeSelectedItem(item);
                      } else {
                        setSelectedItems([...selectedItems, item]);
                        setInputValue('');
                      }
                    },
                  })}
                >
                  <Checkbox tag="span" />
                  {item.value}
                </ListboxItem>
              ))}
            </Listbox>
          </UtilityFragment>
        </ListboxContainer>
      </Combobox>
      <Utility className="v-input-container" vMarginTop={10}>
        <Checkbox
          id={`${id}-checkbox-mark-as-disabled`}
          onChange={() => setIsDisabled(currentValue => !currentValue)}
          checked={isDisabled}
        />
        <Label htmlFor={`${id}-checkbox-mark-as-disabled`}>Mark input as disabled</Label>
      </Utility>
    </>
  );
};

```

### Read-only multiselect
- **Section**: Default multiselects
- **URL**: components/multiselect/read-only-multiselect
- **Tags**: docs
```tsx
import { VisaChevronDownTiny, VisaChevronUpTiny, VisaClearAltTiny } from '@visa/nova-icons-react';
import {
  Button,
  Checkbox,
  Chip,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox, useMultipleSelection } from 'downshift';
import { useState } from 'react';

type Item = { value: string };

const id = 'read-only-multiselect';
const multiselectItems: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const comboboxStateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) => {
  switch (type) {
    case useCombobox.stateChangeTypes.InputClick:
      return {
        // don't open the menu just because the input was clicked
        // instead, wait for an keystroke or a toggle button click
        ...state,
      };
    case useCombobox.stateChangeTypes.InputChange:
      return {
        ...changes,
        // don't update the highlighted index
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.ItemMouseMove:
    case useCombobox.stateChangeTypes.MenuMouseLeave:
      return {
        ...changes,
        // don't change the focused item just because the mouse moved
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.InputKeyDownEnter:
    case useCombobox.stateChangeTypes.ItemClick:
      return {
        ...changes,
        isOpen: true, // keep the menu open on item select or Enter press
        // and if we're selecting an item, maintain the same highlightedIndex
        ...(changes.selectedItem && { highlightedIndex: state.highlightedIndex }),
      };
    default:
      return changes;
  }
};

export const ReadOnlyMultiselect = () => {
  const [inputValue, setInputValue] = useState('');
  const [selectedItems, setSelectedItems] = useState<Item[]>([]);
  const [isReadOnly, setIsReadOnly] = useState(true);

  const items = multiselectItems;

  const { getDropdownProps, removeSelectedItem } = useMultipleSelection({
    selectedItems,
    onStateChange({ selectedItems: newSelectedItems, type }) {
      if (
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownDelete ||
        type === useMultipleSelection.stateChangeTypes.DropdownKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.FunctionRemoveSelectedItem
      ) {
        setSelectedItems(newSelectedItems!);
      }
    },
  });
  const {
    getToggleButtonProps,
    getLabelProps,
    getMenuProps,
    getInputProps,
    getItemProps,
    highlightedIndex,
    isOpen,
    setHighlightedIndex,
  } = useCombobox({
    items,
    itemToString,
    inputValue,
    stateReducer: comboboxStateReducer,
    onStateChange({ inputValue: newInputValue, type, selectedItem }) {
      if (type === useCombobox.stateChangeTypes.InputChange) {
        setInputValue(newInputValue!);
      }
      if (type === useCombobox.stateChangeTypes.ItemClick && !!selectedItem) {
        // make sure the highlighted index is on the item that was just clicked
        setHighlightedIndex(items.indexOf(selectedItem));
      }
    },
  });

  return (
    <>
      <Combobox>
        <UtilityFragment vFlex vFlexCol vGap={4}>
          <DropdownContainer>
            <Label {...getLabelProps()}>Label (required)</Label>
            <UtilityFragment vPaddingVertical={3} vPaddingLeft={3} vPaddingRight={6}>
              <InputContainer>
                <Utility vFlex vFlexGrow vFlexShrink vFlexWrap vGap={2}>
                  {selectedItems.map((item, index) => (
                    <UtilityFragment vFlexShrink0 key={`selected-item-${index}`}>
                      <Chip chipSize="compact">
                        {isReadOnly ? (
                          item.value
                        ) : (
                          <>
                            <Label>{item.value}</Label>
                            <Button
                              aria-label={`Remove ${item.value}`}
                              colorScheme="tertiary"
                              iconButton
                              onClick={() => removeSelectedItem(item)}
                              subtle
                            >
                              <VisaClearAltTiny />
                            </Button>
                          </>
                        )}
                      </Chip>
                    </UtilityFragment>
                  ))}
                  <UtilityFragment vFlexShrink style={{ flexBasis: '50px' }}>
                    <Input
                      name={id}
                      readOnly={isReadOnly}
                      {...getInputProps(
                        getDropdownProps({
                          onKeyDown: e => {
                            if (e.key === 'Enter') {
                              if (highlightedIndex !== -1 && isOpen) {
                                const selectedItem = items[highlightedIndex];
                                if (selectedItems.includes(selectedItem)) {
                                  removeSelectedItem(selectedItem);
                                } else {
                                  setSelectedItems([...selectedItems, selectedItem]);
                                  setInputValue('');
                                }
                              }
                            }
                          },
                        })
                      )}
                    />
                  </UtilityFragment>
                </Utility>
                <Button
                  aria-haspopup="listbox"
                  aria-label={`${id}-toggle-button`}
                  buttonSize="small"
                  colorScheme="tertiary"
                  iconButton
                  disabled={isReadOnly}
                  {...getToggleButtonProps()}
                >
                  {isOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />}
                </Button>
              </InputContainer>
            </UtilityFragment>
          </DropdownContainer>
        </UtilityFragment>
        <ListboxContainer>
          <UtilityFragment vFlex>
            <Listbox {...getMenuProps()}>
              {items.map((item, index) => (
                <ListboxItem<HTMLLIElement>
                  key={`${id}-example-${index}`}
                  className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
                  {...getItemProps({
                    item,
                    index,
                    'aria-selected': selectedItems.includes(item),
                    onClick: () => {
                      if (selectedItems.includes(item)) {
                        removeSelectedItem(item);
                      } else {
                        setSelectedItems([...selectedItems, item]);
                        setInputValue('');
                      }
                    },
                  })}
                >
                  <Checkbox tag="span" />
                  {item.value}
                </ListboxItem>
              ))}
            </Listbox>
          </UtilityFragment>
        </ListboxContainer>
      </Combobox>
      <Utility className="v-input-container" vMarginTop={10}>
        <Checkbox
          id={`${id}-checkbox-mark-as-read-only`}
          onChange={() => setIsReadOnly(currentValue => !currentValue)}
          checked={isReadOnly}
        />
        <Label htmlFor={`${id}-checkbox-mark-as-read-only`}>Mark input as read-only</Label>
      </Utility>
    </>
  );
};

```

### Multiselect without dropdown chevron
- **Section**: Default multiselects
- **URL**: components/multiselect/multiselect-without-dropdown-chevron
- **Tags**: docs
```tsx
import { VisaClearAltTiny } from '@visa/nova-icons-react';
import {
  Button,
  Checkbox,
  Chip,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox, useMultipleSelection } from 'downshift';
import { useState } from 'react';

type Item = { value: string };

const id = 'multiselect-without-dropdown-chevron';
const multiselectItems: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const comboboxStateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) => {
  switch (type) {
    case useCombobox.stateChangeTypes.InputClick:
      return {
        // don't open the menu just because the input was clicked
        // instead, wait for an keystroke or a toggle button click
        ...state,
      };
    case useCombobox.stateChangeTypes.InputChange:
      return {
        ...changes,
        // don't update the highlighted index
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.ItemMouseMove:
    case useCombobox.stateChangeTypes.MenuMouseLeave:
      return {
        ...changes,
        // don't change the focused item just because the mouse moved
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.InputKeyDownEnter:
    case useCombobox.stateChangeTypes.ItemClick:
      return {
        ...changes,
        isOpen: true, // keep the menu open on item select or Enter press
        // and if we're selecting an item, maintain the same highlightedIndex
        ...(changes.selectedItem && { highlightedIndex: state.highlightedIndex }),
      };
    default:
      return changes;
  }
};

export const MultiselectWithoutDropdownChevron = () => {
  const [inputValue, setInputValue] = useState('');
  const [selectedItems, setSelectedItems] = useState<Item[]>([]);
  const items = multiselectItems;

  const { getDropdownProps, removeSelectedItem } = useMultipleSelection({
    selectedItems,
    onStateChange({ selectedItems: newSelectedItems, type }) {
      if (
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownDelete ||
        type === useMultipleSelection.stateChangeTypes.DropdownKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.FunctionRemoveSelectedItem
      ) {
        setSelectedItems(newSelectedItems!);
      }
    },
  });
  const { getLabelProps, getMenuProps, getInputProps, getItemProps, highlightedIndex, isOpen, setHighlightedIndex } =
    useCombobox({
      items,
      itemToString,
      inputValue,
      stateReducer: comboboxStateReducer,
      onStateChange({ inputValue: newInputValue, type, selectedItem }) {
        if (type === useCombobox.stateChangeTypes.InputChange) {
          setInputValue(newInputValue!);
        }
        if (type === useCombobox.stateChangeTypes.ItemClick && !!selectedItem) {
          // make sure the highlighted index is on the item that was just clicked
          setHighlightedIndex(items.indexOf(selectedItem));
        }
      },
    });

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label (required)</Label>
          <UtilityFragment vPaddingVertical={3} vPaddingLeft={3} vPaddingRight={6}>
            <InputContainer>
              <Utility vFlex vFlexGrow vFlexShrink vFlexWrap vGap={2}>
                {selectedItems.map((item, index) => (
                  <UtilityFragment vFlexShrink0 key={`selected-item-${index}`}>
                    <Chip chipSize="compact">
                      <Label>{item.value}</Label>
                      <Button
                        aria-label={`Remove ${item.value}`}
                        colorScheme="tertiary"
                        iconButton
                        onClick={() => removeSelectedItem(item)}
                        subtle
                      >
                        <VisaClearAltTiny />
                      </Button>
                    </Chip>
                  </UtilityFragment>
                ))}
                <UtilityFragment vFlexShrink style={{ flexBasis: '50px' }}>
                  <Input
                    name={id}
                    {...getInputProps(
                      getDropdownProps({
                        onKeyDown: e => {
                          if (e.key === 'Enter') {
                            if (highlightedIndex !== -1 && isOpen) {
                              const selectedItem = items[highlightedIndex];
                              if (selectedItems.includes(selectedItem)) {
                                removeSelectedItem(selectedItem);
                              } else {
                                setSelectedItems([...selectedItems, selectedItem]);
                                setInputValue('');
                              }
                            }
                          }
                        },
                      })
                    )}
                  />
                </UtilityFragment>
              </Utility>
            </InputContainer>
          </UtilityFragment>
        </DropdownContainer>
      </UtilityFragment>
      <ListboxContainer>
        <UtilityFragment vFlex>
          <Listbox {...getMenuProps()}>
            {items.map((item, index) => (
              <ListboxItem<HTMLLIElement>
                key={`${id}-example-${index}`}
                className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
                {...getItemProps({
                  item,
                  index,
                  'aria-selected': selectedItems.includes(item),
                  onClick: () => {
                    if (selectedItems.includes(item)) {
                      removeSelectedItem(item);
                    } else {
                      setSelectedItems([...selectedItems, item]);
                      setInputValue('');
                    }
                  },
                })}
              >
                <Checkbox tag="span" />
                {item.value}
              </ListboxItem>
            ))}
          </Listbox>
        </UtilityFragment>
      </ListboxContainer>
    </Combobox>
  );
};

```

### Multiselect with multiple selections and vertical scroll
- **Section**: Default multiselects
- **URL**: components/multiselect/multiselect-with-multiple-selections-and-vertical-scroll
- **Tags**: docs
```tsx
import { VisaChevronDownTiny, VisaChevronUpTiny, VisaClearAltTiny } from '@visa/nova-icons-react';
import {
  Button,
  Checkbox,
  Chip,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox, useMultipleSelection } from 'downshift';
import { useState } from 'react';

type Item = { value: string };

const id = 'multiselect-with-multiple-selections-and-vertical-scroll';
const multiselectItems: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
  { value: 'Option F' },
  { value: 'Option G' },
  { value: 'Option H' },
  { value: 'Option I' },
  { value: 'Option J' },
  { value: 'Option K' },
  { value: 'Option L' },
  { value: 'Option M' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const comboboxStateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) => {
  switch (type) {
    case useCombobox.stateChangeTypes.InputClick:
      return {
        // don't open the menu just because the input was clicked
        // instead, wait for an keystroke or a toggle button click
        ...state,
      };
    case useCombobox.stateChangeTypes.InputChange:
      return {
        ...changes,
        // don't update the highlighted index
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.ItemMouseMove:
    case useCombobox.stateChangeTypes.MenuMouseLeave:
      return {
        ...changes,
        // don't change the focused item just because the mouse moved
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.InputKeyDownEnter:
    case useCombobox.stateChangeTypes.ItemClick:
      return {
        ...changes,
        isOpen: true, // keep the menu open on item select or Enter press
        // and if we're selecting an item, maintain the same highlightedIndex
        ...(changes.selectedItem && { highlightedIndex: state.highlightedIndex }),
      };
    default:
      return changes;
  }
};

export const MultiselectWithMultipleSelectionsAndVerticalScroll = () => {
  const items = multiselectItems;
  const [inputValue, setInputValue] = useState('');

  // preselect the first 11 items to demonstrate a very full input field with scrollbar
  const [selectedItems, setSelectedItems] = useState<Item[]>(items.slice(0, 12));

  const { getDropdownProps, removeSelectedItem } = useMultipleSelection({
    selectedItems,
    onStateChange({ selectedItems: newSelectedItems, type }) {
      if (
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownDelete ||
        type === useMultipleSelection.stateChangeTypes.DropdownKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.FunctionRemoveSelectedItem
      ) {
        setSelectedItems(newSelectedItems!);
      }
    },
  });
  const {
    getToggleButtonProps,
    getLabelProps,
    getMenuProps,
    getInputProps,
    getItemProps,
    highlightedIndex,
    isOpen,
    setHighlightedIndex,
  } = useCombobox({
    items,
    itemToString,
    inputValue,
    stateReducer: comboboxStateReducer,
    onStateChange({ inputValue: newInputValue, type, selectedItem }) {
      if (type === useCombobox.stateChangeTypes.InputChange) {
        setInputValue(newInputValue!);
      }
      if (type === useCombobox.stateChangeTypes.ItemClick && !!selectedItem) {
        // make sure the highlighted index is on the item that was just clicked
        setHighlightedIndex(items.indexOf(selectedItem));
      }
    },
  });

  return (
    <Combobox style={{ maxInlineSize: '290px' }}>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label (required)</Label>
          <UtilityFragment vPaddingVertical={3} vPaddingLeft={3} vPaddingRight={6}>
            <InputContainer>
              <Utility
                vFlex
                vFlexGrow
                vFlexShrink
                vFlexWrap
                vGap={2}
                style={{ maxBlockSize: '140px', overflowY: 'auto' }}
              >
                {selectedItems.map((item, index) => (
                  <UtilityFragment vFlexShrink0 key={`selected-item-${index}`}>
                    <Chip chipSize="compact">
                      <Label>{item.value}</Label>
                      <Button
                        aria-label={`Remove ${item.value}`}
                        colorScheme="tertiary"
                        iconButton
                        onClick={() => removeSelectedItem(item)}
                        subtle
                      >
                        <VisaClearAltTiny />
                      </Button>
                    </Chip>
                  </UtilityFragment>
                ))}
                <UtilityFragment vFlexShrink style={{ flexBasis: '50px' }}>
                  <Input
                    name={id}
                    {...getInputProps(
                      getDropdownProps({
                        onKeyDown: e => {
                          if (e.key === 'Enter') {
                            if (highlightedIndex !== -1 && isOpen) {
                              const selectedItem = items[highlightedIndex];
                              if (selectedItems.includes(selectedItem)) {
                                removeSelectedItem(selectedItem);
                              } else {
                                setSelectedItems([...selectedItems, selectedItem]);
                                setInputValue('');
                              }
                            }
                          }
                        },
                      })
                    )}
                  />
                </UtilityFragment>
              </Utility>
              <Button
                aria-haspopup="listbox"
                aria-label={`${id}-toggle-button`}
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
        <UtilityFragment vFlex>
          <Listbox scroll {...getMenuProps()}>
            {items.map((item, index) => (
              <ListboxItem<HTMLLIElement>
                key={`${id}-example-${index}`}
                className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
                {...getItemProps({
                  item,
                  index,
                  'aria-selected': selectedItems.includes(item),
                  onClick: () => {
                    if (selectedItems.includes(item)) {
                      removeSelectedItem(item);
                    } else {
                      setSelectedItems([...selectedItems, item]);
                      setInputValue('');
                    }
                  },
                })}
              >
                <Checkbox tag="span" />
                {item.value}
              </ListboxItem>
            ))}
          </Listbox>
        </UtilityFragment>
      </ListboxContainer>
    </Combobox>
  );
};

```

### Multiselect with select and unselect all buttons
- **Section**: Default multiselects
- **URL**: components/multiselect/multiselect-with-select-and-unselect-all-buttons
- **Tags**: docs
```tsx
import { VisaChevronDownTiny, VisaChevronUpTiny, VisaClearAltTiny } from '@visa/nova-icons-react';
import {
  Button,
  Checkbox,
  Chip,
  Combobox,
  Divider,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox, useMultipleSelection } from 'downshift';
import { useState } from 'react';

type Item = { value: string };

const id = 'multiselect-with-select-and-unselect-all-buttons';
const multiselectItems: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const comboboxStateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) => {
  switch (type) {
    case useCombobox.stateChangeTypes.InputClick:
      return {
        // don't open the menu just because the input was clicked
        // instead, wait for an keystroke or a toggle button click
        ...state,
      };
    case useCombobox.stateChangeTypes.InputChange:
      return {
        ...changes,
        // don't update the highlighted index
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.ItemMouseMove:
    case useCombobox.stateChangeTypes.MenuMouseLeave:
      return {
        ...changes,
        // don't change the focused item just because the mouse moved
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.InputKeyDownEnter:
    case useCombobox.stateChangeTypes.ItemClick:
      return {
        ...changes,
        // if an item was selected/removed, keep the menu open and maintain the same highlightedIndex
        ...(changes.selectedItem && { isOpen: true, highlightedIndex: state.highlightedIndex }),
      };
    case useCombobox.stateChangeTypes.InputBlur: // Keep the menu open for focusing on the select/clear all buttons
      return {
        ...changes,
        isOpen: true, // keep the menu open on item select or Enter press
        // and if we're selecting an item, maintain the same highlightedIndex
        ...(changes.selectedItem && { highlightedIndex: state.highlightedIndex }),
      };

    default:
      return changes;
  }
};

export const MultiselectWithSelectAndUnselectAllButtons = () => {
  const [inputValue, setInputValue] = useState('');
  const [selectedItems, setSelectedItems] = useState<Item[]>([]);
  const items = multiselectItems;

  const { getDropdownProps, removeSelectedItem } = useMultipleSelection({
    selectedItems,
    onStateChange({ selectedItems: newSelectedItems, type }) {
      if (
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownDelete ||
        type === useMultipleSelection.stateChangeTypes.DropdownKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.FunctionRemoveSelectedItem
      ) {
        setSelectedItems(newSelectedItems!);
      }
    },
  });
  const {
    getToggleButtonProps,
    getLabelProps,
    getMenuProps,
    getInputProps,
    getItemProps,
    highlightedIndex,
    isOpen,
    setHighlightedIndex,
  } = useCombobox({
    items,
    itemToString,
    inputValue,
    stateReducer: comboboxStateReducer,
    onStateChange({ inputValue: newInputValue, type, selectedItem }) {
      if (type === useCombobox.stateChangeTypes.InputChange) {
        setInputValue(newInputValue!);
      }
      if (type === useCombobox.stateChangeTypes.ItemClick && !!selectedItem) {
        // make sure the highlighted index is on the item that was just clicked
        setHighlightedIndex(items.indexOf(selectedItem));
      }
    },
  });

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label (required)</Label>
          <UtilityFragment vPaddingVertical={3} vPaddingLeft={3} vPaddingRight={6}>
            <InputContainer>
              <Utility vFlex vFlexGrow vFlexShrink vFlexWrap vGap={2}>
                {selectedItems.map((item, index) => (
                  <UtilityFragment vFlexShrink0 key={`selected-item-${index}`}>
                    <Chip chipSize="compact">
                      <Label>{item.value}</Label>
                      <Button
                        aria-label={`Remove ${item.value}`}
                        colorScheme="tertiary"
                        iconButton
                        onClick={() => removeSelectedItem(item)}
                        subtle
                      >
                        <VisaClearAltTiny />
                      </Button>
                    </Chip>
                  </UtilityFragment>
                ))}
                <UtilityFragment vFlexShrink style={{ flexBasis: '50px' }}>
                  <Input
                    name={id}
                    {...getInputProps(
                      getDropdownProps({
                        onKeyDown: e => {
                          if (e.key === 'Enter') {
                            if (highlightedIndex !== -1 && isOpen) {
                              const selectedItem = items[highlightedIndex];
                              if (selectedItems.includes(selectedItem)) {
                                removeSelectedItem(selectedItem);
                              } else {
                                setSelectedItems([...selectedItems, selectedItem]);
                                setInputValue('');
                              }
                            }
                          }
                        },
                      })
                    )}
                  />
                </UtilityFragment>
              </Utility>
              <Button
                aria-haspopup="listbox"
                aria-label={`${id}-toggle-button`}
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
        <>
          <Utility vFlex vJustifyContent="between" vAlignItems="center" vPaddingHorizontal={8}>
            <Button colorScheme="tertiary" onClick={() => setSelectedItems(multiselectItems)}>
              Select All
            </Button>
            <Button colorScheme="tertiary" destructive onClick={() => setSelectedItems([])}>
              Clear All
            </Button>
          </Utility>
          <Divider dividerType="decorative" />
        </>
        <UtilityFragment vFlex>
          <Listbox {...getMenuProps()}>
            {items.map((item, index) => (
              <ListboxItem<HTMLLIElement>
                key={`${id}-example-${index}`}
                className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
                {...getItemProps({
                  item,
                  index,
                  'aria-selected': selectedItems.includes(item),
                  onClick: () => {
                    if (selectedItems.includes(item)) {
                      removeSelectedItem(item);
                    } else {
                      setSelectedItems([...selectedItems, item]);
                      setInputValue('');
                    }
                  },
                })}
              >
                <Checkbox tag="span" />
                {item.value}
              </ListboxItem>
            ))}
          </Listbox>
        </UtilityFragment>
      </ListboxContainer>
    </Combobox>
  );
};

```

### Multiselect with scrollbar
- **Section**: Default multiselects
- **URL**: components/multiselect/multiselect-with-scrollbar
- **Tags**: docs
```tsx
import { VisaChevronDownTiny, VisaChevronUpTiny, VisaClearAltTiny } from '@visa/nova-icons-react';
import {
  Button,
  Checkbox,
  Chip,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox, useMultipleSelection } from 'downshift';
import { useState } from 'react';

type Item = { value: string };

const id = 'multiselect-with-scrollbar';
const multiselectItems: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
  { value: 'Option F' },
  { value: 'Option G' },
  { value: 'Option H' },
  { value: 'Option I' },
  { value: 'Option J' },
  { value: 'Option K' },
  { value: 'Option L' },
  { value: 'Option M' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const comboboxStateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) => {
  switch (type) {
    case useCombobox.stateChangeTypes.InputClick:
      return {
        // don't open the menu just because the input was clicked
        // instead, wait for an keystroke or a toggle button click
        ...state,
      };
    case useCombobox.stateChangeTypes.InputChange:
      return {
        ...changes,
        // don't update the highlighted index
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.ItemMouseMove:
    case useCombobox.stateChangeTypes.MenuMouseLeave:
      return {
        ...changes,
        // don't change the focused item just because the mouse moved
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.InputKeyDownEnter:
    case useCombobox.stateChangeTypes.ItemClick:
      return {
        ...changes,
        isOpen: true, // keep the menu open on item select or Enter press
        // and if we're selecting an item, maintain the same highlightedIndex
        ...(changes.selectedItem && { highlightedIndex: state.highlightedIndex }),
      };
    default:
      return changes;
  }
};

export const MultiselectWithScrollbar = () => {
  const [inputValue, setInputValue] = useState('');
  const [selectedItems, setSelectedItems] = useState<Item[]>([]);
  const items = multiselectItems;

  const { getDropdownProps, removeSelectedItem } = useMultipleSelection({
    selectedItems,
    onStateChange({ selectedItems: newSelectedItems, type }) {
      if (
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownDelete ||
        type === useMultipleSelection.stateChangeTypes.DropdownKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.FunctionRemoveSelectedItem
      ) {
        setSelectedItems(newSelectedItems!);
      }
    },
  });
  const {
    getToggleButtonProps,
    getLabelProps,
    getMenuProps,
    getInputProps,
    getItemProps,
    highlightedIndex,
    isOpen,
    setHighlightedIndex,
  } = useCombobox({
    items,
    itemToString,
    inputValue,
    stateReducer: comboboxStateReducer,
    onStateChange({ inputValue: newInputValue, type, selectedItem }) {
      if (type === useCombobox.stateChangeTypes.InputChange) {
        setInputValue(newInputValue!);
      }
      if (type === useCombobox.stateChangeTypes.ItemClick && !!selectedItem) {
        // make sure the highlighted index is on the item that was just clicked
        setHighlightedIndex(items.indexOf(selectedItem));
      }
    },
  });

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label (required)</Label>
          <UtilityFragment vPaddingVertical={3} vPaddingLeft={3} vPaddingRight={6}>
            <InputContainer>
              <Utility vFlex vFlexGrow vFlexShrink vFlexWrap vGap={2}>
                {selectedItems.map((item, index) => (
                  <UtilityFragment vFlexShrink0 key={`selected-item-${index}`}>
                    <Chip chipSize="compact">
                      <Label>{item.value}</Label>
                      <Button
                        aria-label={`Remove ${item.value}`}
                        colorScheme="tertiary"
                        iconButton
                        onClick={() => removeSelectedItem(item)}
                        subtle
                      >
                        <VisaClearAltTiny />
                      </Button>
                    </Chip>
                  </UtilityFragment>
                ))}
                <UtilityFragment vFlexShrink style={{ flexBasis: '50px' }}>
                  <Input
                    name={id}
                    {...getInputProps(
                      getDropdownProps({
                        onKeyDown: e => {
                          if (e.key === 'Enter') {
                            if (highlightedIndex !== -1 && isOpen) {
                              const selectedItem = items[highlightedIndex];
                              if (selectedItems.includes(selectedItem)) {
                                removeSelectedItem(selectedItem);
                              } else {
                                setSelectedItems([...selectedItems, selectedItem]);
                                setInputValue('');
                              }
                            }
                          }
                        },
                      })
                    )}
                  />
                </UtilityFragment>
              </Utility>
              <Button
                aria-haspopup="listbox"
                aria-label={`${id}-toggle-button`}
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
        <UtilityFragment vFlex>
          <Listbox scroll {...getMenuProps()}>
            {items.map((item, index) => (
              <ListboxItem<HTMLLIElement>
                key={`${id}-example-${index}`}
                className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
                {...getItemProps({
                  item,
                  index,
                  'aria-selected': selectedItems.includes(item),
                  onClick: () => {
                    if (selectedItems.includes(item)) {
                      removeSelectedItem(item);
                    } else {
                      setSelectedItems([...selectedItems, item]);
                      setInputValue('');
                    }
                  },
                })}
              >
                <Checkbox tag="span" />
                {item.value}
              </ListboxItem>
            ))}
          </Listbox>
        </UtilityFragment>
      </ListboxContainer>
    </Combobox>
  );
};

```

### Multiselect with filterable menu and manual selection
- **Section**: Multiselect Behaviors
- **URL**: components/multiselect/multiselect-with-filterable-menu-and-manual-selection
- **Tags**: docs
```tsx
import { VisaChevronDownTiny, VisaChevronUpTiny, VisaClearAltTiny } from '@visa/nova-icons-react';
import {
  Button,
  Checkbox,
  Chip,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Typography,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox, useMultipleSelection } from 'downshift';
import { useMemo, useState } from 'react';

type Item = { value: string };

const id = 'multiselect-with-filterable-menu-and-manual-selection';
const multiselectItems: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const comboboxStateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) => {
  switch (type) {
    case useCombobox.stateChangeTypes.InputClick:
      return {
        // don't open the menu just because the input was clicked
        // instead, wait for an keystroke or a toggle button click
        ...state,
      };
    case useCombobox.stateChangeTypes.ItemMouseMove:
    case useCombobox.stateChangeTypes.MenuMouseLeave:
      return {
        ...changes,
        // don't change the focused item just because the mouse moved
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.InputKeyDownEnter:
    case useCombobox.stateChangeTypes.ItemClick:
      return {
        ...changes,
        isOpen: true, // keep the menu open on item select or Enter press
        // and if we're selecting an item, maintain the same highlightedIndex
        ...(changes.selectedItem && { highlightedIndex: state.highlightedIndex }),
      };
    default:
      return changes;
  }
};

export const MultiselectWithFilterableMenuAndManualSelection = () => {
  const [inputValue, setInputValue] = useState('');
  const [selectedItems, setSelectedItems] = useState<Item[]>([]);
  const items = useMemo(
    () => multiselectItems.filter(item => item.value.toLowerCase().includes(inputValue.toLowerCase())),
    [inputValue]
  );

  const { getDropdownProps, removeSelectedItem } = useMultipleSelection({
    selectedItems,
    onStateChange({ selectedItems: newSelectedItems, type }) {
      if (
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownDelete ||
        type === useMultipleSelection.stateChangeTypes.DropdownKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.FunctionRemoveSelectedItem
      ) {
        setSelectedItems(newSelectedItems!);
      }
    },
  });
  const {
    getToggleButtonProps,
    getLabelProps,
    getMenuProps,
    getInputProps,
    getItemProps,
    highlightedIndex,
    isOpen,
    setHighlightedIndex,
  } = useCombobox({
    items,
    itemToString,
    inputValue,
    stateReducer: comboboxStateReducer,
    onStateChange({ inputValue: newInputValue, type, selectedItem }) {
      if (type === useCombobox.stateChangeTypes.InputChange) {
        setInputValue(newInputValue!);
      }
      if (type === useCombobox.stateChangeTypes.ItemClick && !!selectedItem) {
        // make sure the highlighted index is on the item that was just clicked
        setHighlightedIndex(items.indexOf(selectedItem));
      }
    },
  });

  const resultsFound = items.length > 0;

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label (required)</Label>
          <UtilityFragment vPaddingVertical={3} vPaddingLeft={3} vPaddingRight={6}>
            <InputContainer>
              <Utility vFlex vFlexGrow vFlexShrink vFlexWrap vGap={2}>
                {selectedItems.map((item, index) => (
                  <UtilityFragment vFlexShrink0 key={`selected-item-${index}`}>
                    <Chip chipSize="compact">
                      <Label>{item.value}</Label>
                      <Button
                        aria-label={`Remove ${item.value}`}
                        colorScheme="tertiary"
                        iconButton
                        onClick={() => removeSelectedItem(item)}
                        subtle
                      >
                        <VisaClearAltTiny />
                      </Button>
                    </Chip>
                  </UtilityFragment>
                ))}
                <UtilityFragment vFlexShrink style={{ flexBasis: '50px' }}>
                  <Input
                    name={id}
                    {...getInputProps(
                      getDropdownProps({
                        onKeyDown: e => {
                          if (e.key === 'Enter') {
                            if (highlightedIndex !== -1 && resultsFound && isOpen) {
                              const selectedItem = items[highlightedIndex];
                              if (selectedItems.includes(selectedItem)) {
                                removeSelectedItem(selectedItem);
                              } else {
                                setSelectedItems([...selectedItems, selectedItem]);
                                setInputValue('');
                              }
                            }
                          }
                        },
                      })
                    )}
                  />
                </UtilityFragment>
              </Utility>
              <Button
                aria-haspopup="listbox"
                aria-label={`${id}-toggle-button`}
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
        <UtilityFragment
          vAlignItems={resultsFound ? undefined : 'center'}
          vFlex={resultsFound || undefined}
          vJustifyContent={resultsFound ? undefined : 'center'}
          style={resultsFound ? undefined : { minBlockSize: 180 }}
        >
          <Listbox {...getMenuProps()}>
            {items.map((item, index) => (
              <ListboxItem<HTMLLIElement>
                key={`${id}-example-${index}`}
                className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
                {...getItemProps({
                  item,
                  index,
                  'aria-selected': selectedItems.includes(item),
                  onClick: () => {
                    if (selectedItems.includes(item)) {
                      removeSelectedItem(item);
                    } else {
                      setSelectedItems([...selectedItems, item]);
                      setInputValue('');
                    }
                  },
                })}
              >
                <Checkbox tag="span" />
                {item.value}
              </ListboxItem>
            ))}
            {!resultsFound && (
              <li aria-atomic="true" aria-live="assertive">
                <Typography variant="label-large">No results found</Typography>
              </li>
            )}
          </Listbox>
        </UtilityFragment>
      </ListboxContainer>
    </Combobox>
  );
};

```

### Multiselect with filterable menu and automatic selection
- **Section**: Multiselect Behaviors
- **URL**: components/multiselect/multiselect-with-filterable-menu-and-automatic-selection
- **Tags**: docs
```tsx
import { VisaChevronDownTiny, VisaChevronUpTiny, VisaClearAltTiny } from '@visa/nova-icons-react';
import {
  Button,
  Checkbox,
  Chip,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Typography,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox, useMultipleSelection } from 'downshift';
import { useMemo, useState } from 'react';

type Item = { value: string };

const id = 'multiselect-with-filterable-menu-and-automatic-selection';
const multiselectItems: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const comboboxStateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) => {
  switch (type) {
    case useCombobox.stateChangeTypes.InputClick:
      return {
        // don't open the menu just because the input was clicked
        // instead, wait for an keystroke or a toggle button click
        ...state,
      };
    case useCombobox.stateChangeTypes.ItemMouseMove:
    case useCombobox.stateChangeTypes.MenuMouseLeave:
      return {
        ...changes,
        // don't change the focused item just because the mouse moved
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.InputKeyDownEnter:
    case useCombobox.stateChangeTypes.ItemClick:
      return {
        ...changes,
        isOpen: true, // keep the menu open on item select or Enter press
        // and if we're selecting an item, maintain the same highlightedIndex
        ...(changes.selectedItem && { highlightedIndex: state.highlightedIndex }),
      };
    default:
      return changes;
  }
};

export const MultiselectWithFilterableMenuAndAutomaticSelection = () => {
  const [inputValue, setInputValue] = useState('');
  const [selectedItems, setSelectedItems] = useState<Item[]>([]);
  const items = useMemo(
    () => multiselectItems.filter(item => item.value.toLowerCase().includes(inputValue.toLowerCase())),
    [inputValue]
  );

  const { getDropdownProps, removeSelectedItem } = useMultipleSelection({
    selectedItems,
    onStateChange({ selectedItems: newSelectedItems, type }) {
      if (
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownDelete ||
        type === useMultipleSelection.stateChangeTypes.DropdownKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.FunctionRemoveSelectedItem
      ) {
        setSelectedItems(newSelectedItems!);
      }
    },
  });
  const { getToggleButtonProps, getLabelProps, getMenuProps, getInputProps, getItemProps, highlightedIndex, isOpen } =
    useCombobox({
      items,
      itemToString,
      inputValue,
      defaultHighlightedIndex: 0, // after selection, highlight the first item.
      stateReducer: comboboxStateReducer,
      onStateChange({ inputValue: newInputValue, type }) {
        if (type === useCombobox.stateChangeTypes.InputChange) {
          setInputValue(newInputValue!);
        }
      },
    });

  const resultsFound = items.length > 0;

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label (required)</Label>
          <UtilityFragment vPaddingVertical={3} vPaddingLeft={3} vPaddingRight={6}>
            <InputContainer>
              <Utility vFlex vFlexGrow vFlexShrink vFlexWrap vGap={2}>
                {selectedItems.map((item, index) => {
                  return (
                    <UtilityFragment vFlexShrink0 key={`selected-item-${index}`}>
                      <Chip chipSize="compact">
                        <Label>{item.value}</Label>
                        <Button
                          aria-label={`Remove ${item.value}`}
                          colorScheme="tertiary"
                          iconButton
                          onClick={() => removeSelectedItem(item)}
                          subtle
                        >
                          <VisaClearAltTiny />
                        </Button>
                      </Chip>
                    </UtilityFragment>
                  );
                })}
                <UtilityFragment vFlexShrink style={{ flexBasis: '50px' }}>
                  <Input
                    name={id}
                    {...getInputProps(
                      getDropdownProps({
                        onKeyDown: e => {
                          if (e.key === 'Enter') {
                            if (highlightedIndex !== -1 && resultsFound && isOpen) {
                              const selectedItem = items[highlightedIndex];
                              if (selectedItems.includes(selectedItem)) {
                                removeSelectedItem(selectedItem);
                              } else {
                                setSelectedItems([...selectedItems, selectedItem]);
                                setInputValue('');
                              }
                            }
                          }
                        },
                      })
                    )}
                  />
                </UtilityFragment>
              </Utility>
              <Button
                aria-haspopup="listbox"
                aria-label={`${id}-toggle-button`}
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
        <UtilityFragment
          vAlignItems={resultsFound ? undefined : 'center'}
          vFlex={resultsFound || undefined}
          vJustifyContent={resultsFound ? undefined : 'center'}
          style={resultsFound ? undefined : { minBlockSize: 180 }}
        >
          <Listbox {...getMenuProps()}>
            {items.map((item, index) => (
              <ListboxItem<HTMLLIElement>
                key={`${id}-example-${index}`}
                className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
                {...getItemProps({
                  item,
                  index,
                  'aria-selected': selectedItems.includes(item),
                  onClick: () => {
                    if (selectedItems.includes(item)) {
                      removeSelectedItem(item);
                    } else {
                      setSelectedItems([...selectedItems, item]);
                      setInputValue('');
                    }
                  },
                })}
              >
                <Checkbox tag="span" />
                {item.value}
              </ListboxItem>
            ))}
            {!resultsFound && (
              <li aria-atomic="true" aria-live="assertive">
                <Typography variant="label-large">No results found</Typography>
              </li>
            )}
          </Listbox>
        </UtilityFragment>
      </ListboxContainer>
    </Combobox>
  );
};

```

## Property Sections
### button
- **Selector**: <Button />
- **Description**: 

### checkbox
- **Selector**: <Checkbox />
- **Description**: 

### chip
- **Selector**: <Chip />
- **Description**: 

### combobox
- **Selector**: <Combobox />
- **Description**: 

### divider
- **Selector**: <Divider />
- **Description**: 

### input
- **Selector**: <Input />
- **Description**: 

### listbox
- **Selector**: <Listbox />
- **Description**: 

### typography
- **Selector**: <Typography />
- **Description**: 

