# date-and-time-selectors

## Metadata
- **Version**: 0.0.1
- **Description**: 
- **Category**: components

## Example Sections
1. **Date selectors**
   - Description: 
2. **Date Range Selectors**
   - Description: 
3. **Time selectors**
   - Description: 

## Examples
### Default date selector
- **Section**: Date selectors
- **URL**: components/date-and-time-selectors/default-date-selector
- **Tags**: 
```tsx
import { Input, InputContainer, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-date-selector';

export const DefaultDateSelector = () => {
  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Input id={id} required type="date" />
      </InputContainer>
    </Utility>
  );
};

```

### Read-only date selector
- **Section**: Date selectors
- **URL**: components/date-and-time-selectors/read-only-date-selector
- **Tags**: 
```tsx
import { Input, InputContainer, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'read-only-date-selector';

export const ReadOnlyDateSelector = () => {
  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Input id={id} required type="date" readOnly />
      </InputContainer>
    </Utility>
  );
};
```

### Disabled date selector
- **Section**: Date selectors
- **URL**: components/date-and-time-selectors/disabled-date-selector
- **Tags**: 
```tsx
import { Input, InputContainer, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'disabled-date-selector';

export const DisabledDateSelector = () => {
  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Input id={id} required type="date" disabled />
      </InputContainer>
    </Utility>
  );
};
```

### Date selector with error
- **Section**: Date selectors
- **URL**: components/date-and-time-selectors/date-selector-with-error
- **Tags**: 
```tsx
import { VisaErrorTiny } from '@visa/nova-icons-react';
import { useState } from 'react';
import { Button, Input, InputContainer, InputMessage, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'date-selector-with-error';

export const DateSelectorWithError = () => {
  const [errorState, setErrorState] = useState(false);

  return (
    <>
      <Utility vFlex vFlexCol vGap={4}>
        <Label htmlFor={id}>Label (required)</Label>
        <InputContainer>
          <Input id={id} required type="date" aria-invalid={errorState} />
        </InputContainer>
        {errorState && (
          <InputMessage aria-atomic="true" aria-live="assertive" id={`${id}-message`} role="alert">
            <VisaErrorTiny />
            This is required text that describes the error in more detail.
          </InputMessage>
        )}
      </Utility>
      <Utility vFlex vGap={12} vMarginTop={16}>
        <Button id={`${id}-submit-button`} onClick={() => setErrorState(true)}>
          Submit
        </Button>
        <Button id={`${id}-reset-button`} colorScheme="secondary" onClick={() => setErrorState(false)}>
          Reset
        </Button>
      </Utility>
    </>
  );
};

```

### Date selector with disabled dates
- **Section**: Date selectors
- **URL**: components/date-and-time-selectors/min-max-date-input
- **Tags**: 
```tsx
import { Input, InputContainer, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'min-max-date';

export const MinMaxDateInput = () => {
  return (
    <Utility vFlex vFlexWrap vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Input id={id} max="1999-06-29" min="1999-01-27" required type="date" />
      </InputContainer>
    </Utility>
  );
};

```

### Default date range selector
- **Section**: Date Range Selectors
- **URL**: components/date-and-time-selectors/default-date-range-selector
- **Tags**: 
```tsx
import { Input, InputContainer, Label, Utility } from '@visa/nova-react';
import { FormEvent, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-date-range-selector';

export const DefaultDateRangeSelector = () => {
  const [endDate, setEndDate] = useState('');
  const [startDate, setStartDate] = useState('');

  const onDateChange = (event: FormEvent<HTMLInputElement>, isStartDate: boolean) => {
    const { value } = event.currentTarget;
    isStartDate ? setStartDate(value) : setEndDate(value);
  };

  return (
    <Utility vFlex vFlexWrap vGap="12">
      <Utility vFlex vGap="4" vFlexCol vFlexGrow>
        <Label htmlFor={`${id}-start-date`}>Start Date Label (required)</Label>
        <InputContainer>
          <Input
            id={`${id}-start-date`}
            max={endDate ? endDate : undefined}
            onChange={event => onDateChange(event, true)}
            required
            type="date"
          />
        </InputContainer>
      </Utility>
      <Utility vFlex vGap="4" vFlexCol vFlexGrow>
        <Label htmlFor={`${id}-end-date`}>End Date Label (required)</Label>
        <InputContainer>
          <Input
            id={`${id}-end-date`}
            min={startDate ? startDate : undefined}
            onChange={event => onDateChange(event, false)}
            required
            type="date"
          />
        </InputContainer>
      </Utility>
    </Utility>
  );
};

```

### Stacked date range selector
- **Section**: Date Range Selectors
- **URL**: components/date-and-time-selectors/stacked-date-range-selector
- **Tags**: 
```tsx
import { Input, InputContainer, Label, Utility } from '@visa/nova-react';
import { FormEvent, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'stacked-date-range-selector';

export const StackedDateRangeSelector = () => {
  const [endDate, setEndDate] = useState('');
  const [startDate, setStartDate] = useState('');

  const onDateChange = (event: FormEvent<HTMLInputElement>, isStartDate: boolean) => {
    const { value } = event.currentTarget;
    isStartDate ? setStartDate(value) : setEndDate(value);
  };

  return (
    <Utility vFlex vFlexCol vGap="12">
      <Utility vFlex vGap="4" vFlexCol vFlexGrow>
        <Label htmlFor={`${id}-start-date`}>Start Date Label (required)</Label>
        <InputContainer>
          <Input
            id={`${id}-start-date`}
            max={endDate ? endDate : undefined}
            onChange={event => onDateChange(event, true)}
            required
            type="date"
          />
        </InputContainer>
      </Utility>
      <Utility vFlex vGap="4" vFlexCol vFlexGrow>
        <Label htmlFor={`${id}-end-date`}>End Date Label (required)</Label>
        <InputContainer>
          <Input
            id={`${id}-end-date`}
            min={startDate ? startDate : undefined}
            onChange={event => onDateChange(event, false)}
            required
            type="date"
          />
        </InputContainer>
      </Utility>
    </Utility>
  );
};
```

### Default time selector
- **Section**: Time selectors
- **URL**: components/date-and-time-selectors/default-time-selector
- **Tags**: 
```tsx
import { Input, InputContainer, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-time-selector';

export const DefaultTimeSelector = () => {
  return (
      <Utility vFlex vGap="4" vFlexCol vFlexGrow>
        <Label htmlFor={`${id}-time`}>Label (required)</Label>
        <InputContainer>
          <Input id={`${id}-time`} required type="time" />
        </InputContainer>
      </Utility>
  );
};

```

### Read-only time selector
- **Section**: Time selectors
- **URL**: components/date-and-time-selectors/read-only-time-selector
- **Tags**: 
```tsx
import { Input, InputContainer, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'read-only-time-selector';

export const ReadOnlyTimeSelector = () => {
  return (
      <Utility vFlex vGap="4" vFlexCol vFlexGrow>
        <Label htmlFor={`${id}-time`}>Label (required)</Label>
        <InputContainer>
          <Input id={`${id}-time`} required type="time" readOnly/>
        </InputContainer>
      </Utility>
  );
};

```

### Disabled time selector
- **Section**: Time selectors
- **URL**: components/date-and-time-selectors/disabled-time-selector
- **Tags**: 
```tsx
import { Input, InputContainer, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'disabled-time-selector';

export const DisabledTimeSelector = () => {
  return (
      <Utility vFlex vGap="4" vFlexCol vFlexGrow>
        <Label htmlFor={`${id}-time`}>Label (required)</Label>
        <InputContainer>
          <Input id={`${id}-time`} required type="time" disabled/>
        </InputContainer>
      </Utility>
  );
};

```

### Time selector with error
- **Section**: Time selectors
- **URL**: components/date-and-time-selectors/time-selector-with-error
- **Tags**: 
```tsx
import { VisaErrorTiny } from '@visa/nova-icons-react';
import { useState } from 'react';
import { Button, Input, InputContainer, InputMessage, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'time-selector-with-error';

export const TimeSelectorWithError = () => {
  const [errorState, setErrorState] = useState(false);

  return (
    <>
      <Utility vFlex vGap="4" vFlexCol vFlexGrow>
        <Label htmlFor={`${id}-time`}>Label (required)</Label>
        <InputContainer>
          <Input id={`${id}-time`} required type="time" aria-invalid={errorState} />
        </InputContainer>
        {errorState && (
          <InputMessage aria-atomic="true" aria-live="assertive" id={`${id}-message`} role="alert">
            <VisaErrorTiny />
            This is required text that describes the error in more detail.
          </InputMessage>
        )}
      </Utility>
      <Utility vFlex vGap={12} vMarginTop={16}>
        <Button id={`${id}-submit-button`} onClick={() => setErrorState(true)}>
          Submit
        </Button>
        <Button id={`${id}-reset-button`} colorScheme="secondary" onClick={() => setErrorState(false)}>
          Reset
        </Button>
      </Utility>
    </>
  );
};

```

## Property Sections
### input
- **Selector**: <Input />
- **Description**: 

