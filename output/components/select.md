# select

## Metadata
- **Version**: 0.0.1
- **Description**: HTML element that allows users to select one option from a list.
- **Category**: components

## Example Sections
1. **Default selects**
   - Description: 
2. **Custom selects**
   - Description: 

## Examples
### Default select
- **Section**: Default selects
- **URL**: components/select/default-select
- **Tags**: 
```tsx
import { VisaChevronDownTiny } from '@visa/nova-icons-react';
import { InputContainer, InputControl, Label, Select, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-select';

const options = ['Option A', 'Option B', 'Option C', 'Option D', 'Option E'];

export const DefaultSelect = () => {
  return (
    <Utility tag="fieldset" vFlex vFlexCol vGap={6}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Select id={id} name={`${id}-name`}>
          <option hidden value="" />
          {options.map((option, index) => (
            <option key={`${id}-option-${index}`} value={index}>
              {option}
            </option>
          ))}
        </Select>
        <InputControl>
          <VisaChevronDownTiny />
        </InputControl>
      </InputContainer>
    </Utility>
  );
};

```

### Select with inline label
- **Section**: Default selects
- **URL**: components/select/inline-select
- **Tags**: 
```tsx
import { VisaChevronDownTiny } from '@visa/nova-icons-react';
import { InputContainer, InputControl, Label, Select, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'inline-select';

const options = ['Option A', 'Option B', 'Option C', 'Option D', 'Option E'];

export const InlineSelect = () => {
  return (
    <Utility tag="fieldset" vAlignItems="center" vFlex vFlexRow vGap={6}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Select id={id} name={`${id}-name`}>
          <option hidden value="" />
          {options.map((option, index) => (
            <option key={`${id}-option-${index}`} value={index}>
              {option}
            </option>
          ))}
        </Select>
        <InputControl>
          <VisaChevronDownTiny />
        </InputControl>
      </InputContainer>
    </Utility>
  );
};

```

### Select with inline message
- **Section**: Default selects
- **URL**: components/select/select-with-inline-message
- **Tags**: 
```tsx
import { VisaChevronDownTiny } from '@visa/nova-icons-react';
import { InputContainer, InputControl, InputMessage, Label, Select, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'select-with-inline-message';

const options = ['Option A', 'Option B', 'Option C', 'Option D', 'Option E'];

export const SelectWithInlineMessage = () => {
  return (
    <Utility aria-labelledby={`${id}-message`} tag="fieldset" vFlex vFlexCol vGap={6}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Select aria-describedby={`${id}-message`} id={id} name={`${id}-name`}>
          <option hidden value="" />
          {options.map((option, index) => (
            <option key={`${id}-option-${index}`} value={index}>
              {option}
            </option>
          ))}
        </Select>
        <InputControl>
          <VisaChevronDownTiny />
        </InputControl>
      </InputContainer>
      <InputMessage id={`${id}-message`}>This is optional text that describes the label in more detail.</InputMessage>
    </Utility>
  );
};

```

### Select with error
- **Section**: Default selects
- **URL**: components/select/error-select
- **Tags**: 
```tsx
import { VisaChevronDownTiny, VisaErrorTiny } from '@visa/nova-icons-react';
import { ChangeEvent, FormEvent, useRef, useState } from 'react';
import { Button, InputContainer, InputControl, InputMessage, Label, Select, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'error-select';

const options = ['Option A', 'Option B', 'Option C', 'Option D', 'Option E'];

export const ErrorSelect = () => {
  const [invalid, setInvalid] = useState(false);
  const [selectValue, setSelectValue] = useState('');
  const selectRef = useRef<HTMLSelectElement>(null);

  const onReset = (event: FormEvent) => {
    event.preventDefault();
    setInvalid(false);
    setSelectValue('');
  };
  const onSelectChange = (event: ChangeEvent<HTMLSelectElement>) => {
    const { value } = event.currentTarget;
    setInvalid(!value);
    setSelectValue(value);
  };
  const onSubmit = (event: FormEvent) => {
    event.preventDefault();
    const isInvalid = !selectValue;
    setInvalid(isInvalid);
    if (isInvalid) {
      selectRef.current?.focus();
    }
  };

  return (
    <Utility noValidate onReset={onReset} onSubmit={onSubmit} tag="form" vFlex vFlexCol vGap={16}>
      <Utility aria-labelledby={`${id}-message`} tag="fieldset" vFlex vFlexCol vGap={6}>
        <Label htmlFor={id}>Label (required)</Label>
        <InputContainer>
          <Select
            aria-describedby={`${id}-message`}
            aria-invalid={invalid}
            id={id}
            name="full-name"
            onChange={onSelectChange}
            ref={selectRef}
            required
            value={selectValue}
          >
            <option hidden value="" />
            {options.map((option, index) => (
              <option key={`${id}-option-${index}`} value={index}>
                {option}
              </option>
            ))}
          </Select>
          <InputControl>
            <VisaChevronDownTiny />
          </InputControl>
        </InputContainer>
        {invalid && (
          <InputMessage aria-atomic="true" aria-live="assertive" id={`${id}-message`}>
            <VisaErrorTiny />
            This is required text that describes the error in more detail
          </InputMessage>
        )}
      </Utility>
      <Utility vFlex vGap={10}>
        <Button type="submit">Submit</Button>
        <Button colorScheme="secondary" type="reset">
          Reset
        </Button>
      </Utility>
    </Utility>
  );
};

```

### Read-only select
- **Section**: Default selects
- **URL**: components/select/read-only-select
- **Tags**: 
```tsx
import { VisaChevronDownTiny } from '@visa/nova-icons-react';
import { InputContainer, InputControl, Label, Select, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'read-only-select';

const options = ['Option A', 'Option B', 'Option C', 'Option D', 'Option E'];

export const ReadOnlySelect = () => {
  return (
    <Utility tag="fieldset" vFlex vFlexCol vGap={6}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Select defaultValue="0" id={id} name={`${id}-name`} readOnly required>
          <option hidden value="" />
          {options.map((option, index) => (
            <option disabled key={`${id}-option-${index}`} value={index}>
              {option}
            </option>
          ))}
        </Select>
        <InputControl>
          <VisaChevronDownTiny />
        </InputControl>
      </InputContainer>
    </Utility>
  );
};

```

### Disabled select
- **Section**: Default selects
- **URL**: components/select/disabled-select
- **Tags**: 
```tsx
import { VisaChevronDownTiny } from '@visa/nova-icons-react';
import { Checkbox, InputContainer, InputControl, InputMessage, Label, Select, Utility } from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'disabled-select';

const options = ['Option A', 'Option B', 'Option C', 'Option D', 'Option E'];

export const DisabledSelect = () => {
  const [disabled, setDisabled] = useState(true);

  return (
    <Utility vFlex vFlexCol vGap={16}>
      <Utility aria-labelledby={`${id}-message`} tag="fieldset" vFlex vFlexCol vGap={6}>
        <Label htmlFor={id}>Label (required)</Label>
        <InputContainer>
          <Select aria-describedby={`${id}-message`} disabled={disabled} id={id} name={`${id}-name`}>
            <option hidden value="" />
            {options.map((option, index) => (
              <option key={`${id}-option-${index}`} value={index}>
                {option}
              </option>
            ))}
          </Select>
          <InputControl>
            <VisaChevronDownTiny />
          </InputControl>
        </InputContainer>
        <InputMessage id={`${id}-message`}>This is optional text that describes the label in more detail.</InputMessage>
      </Utility>
      <Utility vAlignItems="center" vFlex vGap={2}>
        <Checkbox
          checked={disabled}
          id={`${id}-demo-checkbox`}
          onChange={() => {
            setDisabled(!disabled);
          }}
        />
        <Label htmlFor={`${id}-demo-checkbox`}>Mark select as disabled</Label>
      </Utility>
    </Utility>
  );
};

```

### Select for card expiration
- **Section**: Custom selects
- **URL**: components/select/card-expiration
- **Tags**: custom
```tsx
import { VisaChevronDownTiny, VisaErrorTiny } from '@visa/nova-icons-react';
import {
  Button,
  InputContainer,
  InputControl,
  InputMessage,
  Label,
  Select,
  Typography,
  Utility,
} from '@visa/nova-react';
import { ChangeEvent, FormEvent, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'card-expiration-select';

const today = new Date();
const currentMonth = today.getMonth() + 1;
const currentMonthString = currentMonth.toString();
const currentYear = today.getFullYear();
const currentYearString = currentYear.toString();

const months = Array.from({ length: 12 }, (_, i) => i + 1);
const years = Array.from({ length: 11 }, (_, i) => currentYear + i);

export const CardExpirationSelect = () => {
  const [selectedMonth, setSelectedMonth] = useState('');
  const [selectedYear, setSelectedYear] = useState('');
  const [invalid, setInvalid] = useState(false);

  const onMonthChange = (event: ChangeEvent<HTMLSelectElement>) => {
    setSelectedMonth(event.target.value);
    setInvalid(false);
  };
  const onYearChange = (event: ChangeEvent<HTMLSelectElement>) => {
    setSelectedYear(event.target.value);
    setInvalid(false);
  };

  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
    const isValid = event.currentTarget.checkValidity();

    // If valid, alert with selections
    if (isValid) alert(`Selected Month: ${selectedMonth}\nSelected Year: ${selectedYear}`);
    // If invalid, focus on invalid element
    else (event.currentTarget.querySelector(':not(fieldset):invalid') as HTMLInputElement)?.focus();

    setInvalid(!isValid);
    event.preventDefault();
  };

  return (
    <Utility noValidate onSubmit={onSubmit} tag="form" vFlex vFlexCol vGap={6}>
      <Utility aria-labelledby={`${id}-message`} tag="fieldset" vFlex vFlexCol vGap={4}>
        <Label tag="legend">Expires (MM/YY)</Label>
        <Utility vFlex vFlexRow vAlignItems="center" vGap={6}>
          {/* Month select */}
          <InputContainer>
            <Select
              aria-describedby={`${id}-message`}
              aria-invalid={invalid && selectedMonth === ''}
              aria-label="Expiration month"
              aria-required={true}
              autoComplete="cc-exp-month"
              id={`${id}-month`}
              name={`${id}-month`}
              onChange={onMonthChange}
              required
              value={selectedMonth}
            >
              <option hidden value="" />
              {months.map(month => (
                <option
                  disabled={selectedYear !== '' && selectedYear === currentYearString && month < currentMonth}
                  key={`card-exp-month-${month}`}
                  value={month}
                >
                  {(month < 10 ? '0' : '') + month}
                </option>
              ))}
            </Select>
            <InputControl>
              <VisaChevronDownTiny />
            </InputControl>
          </InputContainer>

          <Typography aria-hidden={true} tag="span" variant="body-1">
            /
          </Typography>

          {/* Year select */}
          <InputContainer>
            <Select
              aria-describedby={`${id}-message`}
              aria-invalid={invalid && selectedYear === ''}
              aria-label="Expiration year"
              aria-required={true}
              autoComplete="cc-exp-year"
              id={`${id}-year`}
              name={`${id}-year`}
              onChange={onYearChange}
              required
              value={selectedYear}
            >
              <option hidden value="" />
              {years.map(year => (
                <option
                  disabled={selectedMonth !== '' && year === currentYear && selectedMonth < currentMonthString}
                  key={`card-exp-year-${year}`}
                  value={year}
                >
                  {year.toString().substring(2)}
                </option>
              ))}
            </Select>
            <InputControl>
              <VisaChevronDownTiny />
            </InputControl>
          </InputContainer>
        </Utility>
        {invalid && (
          <InputMessage aria-atomic="true" aria-live="assertive" id={`${id}-message`}>
            <VisaErrorTiny />
            This is required text that describes the error in more detail
          </InputMessage>
        )}
      </Utility>
      <div>
        <Button type="submit">Submit</Button>
      </div>
    </Utility>
  );
};

```

## Property Sections
### Select
- **Selector**: <Select />
- **Description**: HTML element that allows users to select one option from a list.

## Properties
### ref
- **Section**: Select
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Select
- **Type**: ElementType
- **Default**: select
- **Required**: false
- **Description**: Tag of Component

