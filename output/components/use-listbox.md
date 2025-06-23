# use-listbox

## Metadata
- **Version**: 0.0.1
- **Description**: This hook is used to manage the selected state and keyboard navigation of listbox component.
- **Category**: hooks

## Example Sections
1. **Behavior and usage**
   - Description: 

## Examples
### 
- **Section**: Behavior and usage
- **URL**: hooks/use-listbox/use-listbox-example
- **Tags**: 
```tsx
import { Label, Listbox, ListboxContainer, ListboxItem, useListbox } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'use-listbox-usage';

const options = [
  {
    label: 'Item A',
  },
  {
    disabled: true,
    label: 'Item B',
  },
  {
    label: 'Item C',
  },
  {
    label: 'Item D',
  },
  {
    label: 'Item E',
  },
];

export const UseListboxExample = () => {
  // useListbox hook returns the following:
  // isIndexSelected: function that returns a boolean value to determine if the index is selected or not
  // getTabIndex: function that returns the correct tabIndex based on the index and disabled state
  // onKeyNavigation: function that handles keyboard navigation, and toggles the list item selected state
  // ref: a ref object that is used to store the list item elements
  // toggleIndexSelected: function that toggles the list item selected state, based on the index provided
  const { isIndexSelected, getTabIndex, onKeyNavigation, ref, toggleIndexSelected } = useListbox({
    defaultSelected: 0,
  }); // Default to active on first list item

  return (
    <fieldset>
      <Label id={`${id}-legend`} tag="legend">
        Label (required)
      </Label>
      <ListboxContainer>
        <Listbox aria-labelledby={`${id}-legend`} id={id} onKeyDown={onKeyNavigation} role="listbox" scroll>
          {options.map((option, index) => (
            <ListboxItem
              aria-disabled={option.disabled}
              aria-selected={isIndexSelected(index)}
              key={`${id}-option-${index}`}
              onClick={() => toggleIndexSelected(index)}
              ref={el => {
                ref.current[index] = el;
              }}
              role="option"
              tabIndex={getTabIndex(index, option.disabled)}
            >
              <span className="v-radio v-flex-shrink-0 " />
              {option.label}
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </fieldset>
  );
};

```

