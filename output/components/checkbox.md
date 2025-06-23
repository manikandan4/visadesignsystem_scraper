# checkbox

## Metadata
- **Version**: 0.0.1
- **Description**: Interactive element enabling users to select one or more independent options from a group.
- **Category**: components

## Example Sections
1. **Default checkboxes**
   - Description: 
2. **Checkbox groups**
   - Description: 
3. **Checkbox panels**
   - Description: 
4. **Checkbox panels group**
   - Description: 

## Examples
### Checkbox with label
- **Section**: Default checkboxes
- **URL**: components/checkbox/default-checkbox
- **Tags**: docs
```tsx
import { Checkbox, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'checkbox-default';

export const DefaultCheckbox = () => {
  return (
    <Utility vAlignItems="center" vFlex vGap={2}>
      <Checkbox id={id} />
      <Label htmlFor={id}>Label</Label>
    </Utility>
  );
};

```

### Checkbox without visible label
- **Section**: Default checkboxes
- **URL**: components/checkbox/standalone-checkbox
- **Tags**: docs
```tsx
import { Checkbox, Utility } from '@visa/nova-react';

export const StandaloneCheckbox = () => {
  return (
    <Utility vAlignItems="center" vFlex vGap={2}>
      <Checkbox aria-label="label" />
    </Utility>
  );
};

```

### Checkbox with description
- **Section**: Default checkboxes
- **URL**: components/checkbox/inline-message-checkbox
- **Tags**: docs
```tsx
import { Checkbox, InputMessage, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'inline-message-checkbox';

export const InlineMessageCheckbox = () => {
  return (
    <fieldset aria-labelledby={`${id}-message`}>
      <Utility vFlex vGap={2}>
        <Checkbox id={id} />
        <Utility vFlex vFlexCol vGap={2} vMarginVertical={10}>
          <Label htmlFor={id}>Label</Label>
          <InputMessage id={`${id}-message`}>
            This is optional text that describes the label in more detail.
          </InputMessage>
        </Utility>
      </Utility>
    </fieldset>
  );
};

```

### Checked checkbox
- **Section**: Default checkboxes
- **URL**: components/checkbox/checked-checkbox
- **Tags**: 
```tsx
import { Checkbox, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'checked-checkbox';

export const CheckedCheckbox = () => {
  return (
    <Utility vAlignItems="center" vFlex vGap={2}>
      <Checkbox defaultChecked id={id} />
      <Label htmlFor={id}>Label</Label>
    </Utility>
  );
};

```

### Checkbox with error
- **Section**: Default checkboxes
- **URL**: components/checkbox/validation-checkbox
- **Tags**: docs
```tsx
import { VisaErrorTiny } from '@visa/nova-icons-react';
import { ChangeEvent, useRef, useState } from 'react';
import { Button, Checkbox, InputMessage, Label, Utility, UtilityFragment } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'validation-checkbox';

export const ValidationCheckbox = () => {
  const checkboxRef = useRef<HTMLInputElement>(null);
  const [checked, setChecked] = useState(false);
  const [invalid, setInvalid] = useState(false);

  const onCheckboxChange = (event: ChangeEvent<HTMLInputElement>) => {
    setChecked(event.target.checked);
  };

  const onSubmit = () => {
    if (checked) return setInvalid(false);
    setInvalid(true);
    checkboxRef.current?.focus();
  };

  return (
    <>
      <Utility tag="fieldset" vFlex vFlexCol>
        <Utility vAlignItems="center" vFlex vGap={2}>
          <Checkbox
            aria-describedby={`${id}-message`}
            aria-invalid={invalid}
            aria-required={true}
            checked={checked}
            id={id}
            onChange={onCheckboxChange}
            ref={checkboxRef}
            value="1"
          />
          <Label htmlFor={id}>Label</Label>
        </Utility>
        {invalid && (
          <UtilityFragment vMarginTop={4}>
            <InputMessage aria-atomic="true" aria-live="assertive" id={`${id}-message`} role="alert" variant="body-3">
              <VisaErrorTiny />
              This is required text that describes the error in more detail.
            </InputMessage>
          </UtilityFragment>
        )}
      </Utility>
      <UtilityFragment vMarginTop={12}>
        <Button onClick={onSubmit}>Submit</Button>
      </UtilityFragment>
    </>
  );
};

```

### Disabled checkbox
- **Section**: Default checkboxes
- **URL**: components/checkbox/disabled-unchecked-checkbox
- **Tags**: docs
```tsx
import { Checkbox, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'checkbox-disabled';

export const DisabledUncheckedCheckbox = () => {
  return (
    <Utility vAlignItems="center" vFlex vGap={2}>
      <Checkbox disabled id={id} />
      <Label htmlFor={id}>Label</Label>
    </Utility>
  );
};

```

### Disabled checked checkbox
- **Section**: Default checkboxes
- **URL**: components/checkbox/disabled-checked-checkbox
- **Tags**: docs
```tsx
import { Checkbox, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'checkbox-disabled-checked';

export const DisabledCheckedCheckbox = () => {
  return (
    <Utility vAlignItems="center" vFlex vGap={2}>
      <Checkbox id={id} disabled checked />
      <Label htmlFor={id}>Label</Label>
    </Utility>
  );
};

```

### Checkbox group
- **Section**: Checkbox groups
- **URL**: components/checkbox/group-checkbox
- **Tags**: docs
```tsx
import { Checkbox, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'checkbox-group';

const checkboxes = ['Label 1', 'Label 2', 'Label 3', 'Label 4'];

export const GroupCheckbox = () => {
  return (
    <fieldset aria-labelledby={`${id}-legend`}>
      <Label id={`${id}-legend`} tag="legend">
        Group label
      </Label>
      <Utility tag="ul" vFlex vFlexCol>
        {checkboxes.map((checkbox, index) => (
          <Utility key={`${id}-option-${index}`} tag="li" vAlignItems="center" vFlex vGap={2}>
            <Checkbox id={`${id}-option-${index}`} />
            <Label htmlFor={`${id}-option-${index}`}>{checkbox}</Label>
          </Utility>
        ))}
      </Utility>
    </fieldset>
  );
};

```

### Checkbox group with error
- **Section**: Checkbox groups
- **URL**: components/checkbox/group-with-validation-checkbox
- **Tags**: docs
```tsx
import { VisaErrorTiny } from '@visa/nova-icons-react';
import { Button, Checkbox, InputMessage, Label, Utility, UtilityFragment } from '@visa/nova-react';
import { FormEvent, useRef, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'group-with-validation-checkbox';

type CheckboxStats = {
  checked: boolean;
  label: string;
  required: boolean;
  value: string;
};

const defaultCheckboxStats: CheckboxStats[] = [
  {
    checked: false,
    label: 'Label 1',
    required: true,
    value: 'label-1',
  },
  {
    checked: true,
    label: 'Label 2',
    required: true,
    value: 'label-2',
  },
  {
    checked: false,
    label: 'Label 3',
    required: true,
    value: 'label-3',
  },
  {
    checked: false,
    label: 'Label 4',
    required: true,
    value: 'label-4',
  },
];

export const GroupWithValidationCheckbox = () => {
  const checkboxRefs = useRef<(HTMLInputElement | null)[]>([]);
  const [checkboxStats, setCheckboxStats] = useState(defaultCheckboxStats);
  const [invalid, setInvalid] = useState(false);

  const onCheckboxChange = (event: FormEvent<HTMLInputElement>, index: number) => {
    const { checked } = event.currentTarget;
    const newCheckboxStats = [...checkboxStats];
    newCheckboxStats[index].checked = checked;
    setCheckboxStats(newCheckboxStats);
  };

  const onSubmit = () => {
    // Check if any of the checkbox are checked
    const isInvalid = !checkboxStats.some(checkbox => checkbox.checked);
    // Set invalid state
    setInvalid(isInvalid);
    // If invalid focus on the first checkbox
    if (isInvalid) checkboxRefs.current[0]?.focus();
  };

  return (
    <>
      <fieldset aria-labelledby={`${id}-legend`}>
        <Label aria-describedby={`${id}-message`} id={`${id}-legend`} tag="legend">
          Group label
        </Label>
        <Utility tag="ul" vFlex vFlexCol>
          {checkboxStats.map((checkboxStat, index) => (
            <Utility key={index} tag="li" vAlignItems="center" vFlex vGap={2}>
              <Checkbox
                aria-invalid={invalid}
                checked={checkboxStat.checked}
                id={`${id}-option-${index}`}
                onChange={event => onCheckboxChange(event, index)}
                ref={ref => {
                  checkboxRefs.current[index] = ref;
                }}
                value={checkboxStat.value}
              />
              <Label htmlFor={`${id}-option-${index}`}>{checkboxStat.label}</Label>
            </Utility>
          ))}
        </Utility>

        <UtilityFragment vMarginTop={4}>
          <InputMessage aria-atomic="true" aria-live="assertive" id={`${id}-message`} role="alert" variant="body-3">
            {invalid && (
              <>
                <VisaErrorTiny />
                This is required text that describes the error in more detail.
              </>
            )}
          </InputMessage>
        </UtilityFragment>
      </fieldset>
      <UtilityFragment vMarginTop={12}>
        <Button onClick={onSubmit}>Submit</Button>
      </UtilityFragment>
    </>
  );
};

```

### Indeterminate checkbox group
- **Section**: Checkbox groups
- **URL**: components/checkbox/indeterminate-group-checkbox
- **Tags**: docs
```tsx
import { Checkbox, Label, Utility } from '@visa/nova-react';
import { CSSProperties, forwardRef, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'indeterminate-group-checkbox';

type Option = {
  checked?: boolean;
  children?: Option[];
  disabled?: boolean;
  label: string;
};

// NOTE: This example only works with one level of nesting. A different data structure and way of state management would be required for deeper nesting.
const defaultOptions: Option[] = [
  {
    label: 'L1 label 1',
    children: [
      {
        checked: true,
        label: 'L2 label 1',
      },
      {
        label: 'L2 label 2',
      },
      {
        label: 'L2 label 3',
      },
    ],
  },
];

type CheckboxGroupProps = {
  disabled?: boolean;
  invalid?: boolean;
  onCheckboxChange: (checked: boolean, parentIndex: number | undefined, childIndex: number) => void;
  options: Option[];
  parentId: string;
  parentIndex?: number;
};

const CheckboxGroup = forwardRef<HTMLInputElement, CheckboxGroupProps>(
  ({ disabled, invalid, onCheckboxChange, options, parentId, parentIndex }: CheckboxGroupProps, ref) =>
    options.map((option, index) => {
      const optionId = `${parentId}-option-${index}`;
      const someChildrenChecked = option.children?.some(child => child.checked);
      const someChildrenUnchecked = option.children?.some(child => !child.checked);
      const indeterminate = someChildrenChecked && someChildrenUnchecked;
      return (
        <Utility key={optionId} tag="li" vFlex vFlexCol>
          <Utility vAlignItems="center" vFlex vGap={2}>
            <Checkbox
              aria-invalid={invalid}
              checked={!indeterminate && (option.checked ?? false)}
              disabled={option.disabled || disabled}
              id={optionId}
              indeterminate={indeterminate}
              onChange={event => onCheckboxChange(event.currentTarget.checked, parentIndex, index)}
              ref={index === 0 ? ref : undefined}
            />
            <Label htmlFor={optionId}>{option.label}</Label>
          </Utility>
          {option?.children && (
            <Utility vFlex vFlexCol vMarginLeft={16} tag="ul">
              <CheckboxGroup
                disabled={option.disabled || disabled}
                invalid={invalid}
                onCheckboxChange={onCheckboxChange}
                options={option.children}
                parentId={optionId}
                parentIndex={(parentIndex || 0) + index}
              />
            </Utility>
          )}
        </Utility>
      );
    })
);

CheckboxGroup.displayName = 'CheckboxGroup';

export const IndeterminateGroupCheckbox = () => {
  const [options, setOptions] = useState(defaultOptions);

  const onCheckboxChange = (checked: boolean, parentIndex: number | undefined, childIndex: number) => {
    // Initialize our new options array
    const newOptions = [...options];

    const checkboxGroup = newOptions[parentIndex === undefined ? childIndex : parentIndex];
    const checkboxChild = checkboxGroup?.children && checkboxGroup?.children[childIndex];
    // If parentIndex is undefined then it is a parent checkbox change
    if (parentIndex === undefined) {
      checkboxGroup.checked = checked;
      checkboxGroup.children?.forEach(child => {
        child.checked = checked;
      });
    }
    // If children exist and they're all checked make sure the group is checked
    if (checkboxChild) {
      checkboxChild.checked = checked;
      const allChildrenChecked = checkboxGroup.children?.every(child => child?.checked) || false;
      checkboxGroup.checked = allChildrenChecked;
    }

    // Update the state
    setOptions(newOptions);
  };

  return (
    <fieldset aria-labelledby={`${id}-legend`} style={{ '--v-checkbox-group-gap': '8px' } as CSSProperties}>
      <Label id={`${id}-legend`} tag="legend">
        Group label
      </Label>
      <Utility tag="ul" vFlex vFlexCol>
        <CheckboxGroup onCheckboxChange={onCheckboxChange} options={options} parentId={id} />
      </Utility>
    </fieldset>
  );
};

```

### Error indeterminate checkbox group
- **Section**: Checkbox groups
- **URL**: components/checkbox/error-indeterminate-group-checkbox
- **Tags**: docs
```tsx
import { VisaErrorTiny } from '@visa/nova-icons-react';
import { Button, Checkbox, InputMessage, Label, Utility } from '@visa/nova-react';
import { CSSProperties, forwardRef, useRef, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'error-indeterminate-group-checkbox';

type Option = {
  checked?: boolean;
  children?: Option[];
  disabled?: boolean;
  label: string;
};

// NOTE: This example only works with one level of nesting. A different data structure and way of state management would be required for deeper nesting.
const defaultOptions: Option[] = [
  {
    label: 'L1 label 1',
    children: [
      {
        checked: true,
        label: 'L2 label 1',
      },
      {
        label: 'L2 label 2',
      },
      {
        label: 'L2 label 3',
      },
    ],
  },
];

type CheckboxGroupProps = {
  disabled?: boolean;
  invalid?: boolean;
  onCheckboxChange: (checked: boolean, parentIndex: number | undefined, childIndex: number) => void;
  options: Option[];
  parentId: string;
  parentIndex?: number;
};

const CheckboxGroup = forwardRef<HTMLInputElement, CheckboxGroupProps>(
  ({ disabled, invalid, onCheckboxChange, options, parentId, parentIndex }: CheckboxGroupProps, ref) =>
    options.map((option, index) => {
      const optionId = `${parentId}-option-${index}`;
      const someChildrenChecked = option.children?.some(child => child.checked);
      const someChildrenUnchecked = option.children?.some(child => !child.checked);
      const indeterminate = someChildrenChecked && someChildrenUnchecked;
      return (
        <Utility key={optionId} tag="li" vFlex vFlexCol>
          <Utility vAlignItems="center" vFlex vGap={2}>
            <Checkbox
              aria-invalid={invalid}
              checked={!indeterminate && (option.checked ?? false)}
              disabled={option.disabled || disabled}
              id={optionId}
              indeterminate={indeterminate}
              onChange={event => onCheckboxChange(event.currentTarget.checked, parentIndex, index)}
              ref={index === 0 ? ref : undefined}
            />
            <Label htmlFor={optionId}>{option.label}</Label>
          </Utility>
          {option?.children && (
            <Utility vFlex vFlexCol vMarginLeft={16} tag="ul">
              <CheckboxGroup
                disabled={option.disabled || disabled}
                invalid={invalid}
                onCheckboxChange={onCheckboxChange}
                options={option.children}
                parentId={optionId}
                parentIndex={(parentIndex || 0) + index}
              />
            </Utility>
          )}
        </Utility>
      );
    })
);

CheckboxGroup.displayName = 'CheckboxGroup';

export const ErrorIndeterminateGroupCheckbox = () => {
  const [invalid, setInvalid] = useState(false);
  const [options, setOptions] = useState(defaultOptions);
  const firstFocusableCheckbox = useRef<HTMLInputElement | null>(null);

  const onCheckboxChange = (checked: boolean, parentIndex: number | undefined, childIndex: number) => {
    // Initialize our new options array
    const newOptions = [...options];

    const checkboxGroup = newOptions[parentIndex === undefined ? childIndex : parentIndex];
    const checkboxChild = checkboxGroup?.children && checkboxGroup?.children[childIndex];
    // If parentIndex is undefined then it is a parent checkbox change
    if (parentIndex === undefined) {
      checkboxGroup.checked = checked;
      checkboxGroup.children?.forEach(child => {
        child.checked = checked;
      });
    }
    // If children exist and they're all checked make sure the group is checked
    if (checkboxChild) {
      checkboxChild.checked = checked;
      const allChildrenChecked = checkboxGroup.children?.every(child => child?.checked) || false;
      checkboxGroup.checked = allChildrenChecked;
    }

    // Update the state
    setOptions(newOptions);
  };

  const onSubmit = () => {
    // Check if any of the checkboxes are not checked
    const isInvalid = options.some(option => !option.checked);
    // Set invalid state
    setInvalid(isInvalid);
    // If invalid focus on the first checkbox
    if (isInvalid) firstFocusableCheckbox.current?.focus();
  };

  return (
    <>
      <fieldset aria-labelledby={`${id}-legend`} style={{ '--v-checkbox-group-gap': '8px' } as CSSProperties}>
        <Label aria-describedby={`${id}-message`} id={`${id}-legend`} tag="legend">
          Group label
        </Label>
        <Utility tag="ul" vFlex vFlexCol>
          <CheckboxGroup
            invalid={invalid}
            onCheckboxChange={onCheckboxChange}
            options={options}
            parentId={id}
            ref={firstFocusableCheckbox}
          />
        </Utility>
        <InputMessage aria-atomic="true" aria-live="assertive" id={`${id}-message`} role="alert" variant="body-3">
          {invalid && (
            <>
              <VisaErrorTiny />
              This is required text that describes the error in more detail.
            </>
          )}
        </InputMessage>
      </fieldset>
      <Button className="v-mt-12" onClick={onSubmit}>
        Submit
      </Button>
    </>
  );
};

```

### Horizontal checkbox group
- **Section**: Checkbox groups
- **URL**: components/checkbox/group-horizontal-checkbox
- **Tags**: 
```tsx
import { Checkbox, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'group-horizontal-checkbox';

const checkboxes = ['Label 1', 'Label 2', 'Label 3', 'Label 4'];

export const GroupHorizontalCheckbox = () => {
  return (
    <fieldset aria-labelledby={`${id}-legend`}>
      <Label className="v-label" id={`${id}-legend`} tag="legend">
        Group label
      </Label>
      <Utility tag="ul" vFlex vFlexRow vFlexWrap vGap={24}>
        {checkboxes.map((checkbox, index) => (
          <Utility key={`${id}-option-${index}`} tag="li" vAlignItems="center" vFlex vGap={2}>
            <Checkbox id={`${id}-option-${index}`} />
            <Label htmlFor={`${id}-option-${index}`}>{checkbox}</Label>
          </Utility>
        ))}
      </Utility>
    </fieldset>
  );
};

```

### Checkbox panel
- **Section**: Checkbox panels
- **URL**: components/checkbox/with-description-panel-checkbox
- **Tags**: docs
```tsx
import { Checkbox, CheckboxPanel, InputMessage, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'with-description-panel-checkbox';

export const WithDescriptionPanelCheckbox = () => {
  return (
    <fieldset aria-labelledby={`${id}-message`}>
      <CheckboxPanel htmlFor={id} className="v-align-items-start">
        <Utility vFlex vGap={2} style={{ inlineSize: '100%' }}>
          <Checkbox id={id} name={id} className="v-flex-shrink-0" />
          <Utility vFlex vFlexCol vGap={2} vMarginVertical={8}>
            Label
            <InputMessage id={`${id}-message`}>
              This is optional text that describes the label in more detail.
            </InputMessage>
          </Utility>
        </Utility>
      </CheckboxPanel>
    </fieldset>
  );
};

```

### Checkbox panel without description
- **Section**: Checkbox panels
- **URL**: components/checkbox/without-description-panel-checkbox
- **Tags**: docs
```tsx
import { Checkbox, CheckboxPanel, Utility, UtilityFragment } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'without-description-panel-checkbox';

export const WithoutDescriptionPanelCheckbox = () => {
  return (
    <UtilityFragment vAlignItems="start">
      <CheckboxPanel htmlFor={id}>
        <Utility style={{ inlineSize: '100%' }} vAlignItems="center" vFlex vGap={2}>
          <Checkbox className="v-flex-shrink-0" id={id} name={id} />
          Label
        </Utility>
      </CheckboxPanel>
    </UtilityFragment>
  );
};

```

### Disabled checkbox panel
- **Section**: Checkbox panels
- **URL**: components/checkbox/disabled-panel-checkbox
- **Tags**: docs
```tsx
import { Checkbox, CheckboxPanel, InputMessage, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'checkbox-panel-disabled';

export const DisabledPanelCheckbox = () => {
  return (
    <fieldset aria-labelledby={`${id}-message`}>
      <CheckboxPanel className="v-align-items-start" htmlFor={id}>
        <Utility vFlex vGap={2} style={{ inlineSize: '100%' }}>
          <Checkbox className="v-flex-shrink-0" disabled id={id} name={id} />
          <Utility vFlex vFlexCol vGap={2} vMarginVertical={8}>
            Label
            <InputMessage id={`${id}-message`}>
              This is optional text that describes the label in more detail.
            </InputMessage>
          </Utility>
        </Utility>
      </CheckboxPanel>
    </fieldset>
  );
};

```

### Checkbox panel group
- **Section**: Checkbox panels group
- **URL**: components/checkbox/group-panel-checkbox
- **Tags**: docs
```tsx
import { Checkbox, CheckboxPanel, InputMessage, Typography, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'group-panel-checkbox';

const checkboxes = [
  { label: 'Label 1', message: 'This is optional text that describes the label in more detail.' },
  { label: 'Label 2', message: 'This is optional text that describes the label in more detail.' },
  { label: 'Label 3', message: 'This is optional text that describes the label in more detail.' },
];

export const GroupPanelCheckbox = () => {
  return (
    <fieldset aria-labelledby={`${id}-legend`}>
      <Typography id={`${id}-legend`} tag="legend" variant="label">
        Group Label
      </Typography>
      <Utility vFlex vFlexCol vGap={8}>
        {checkboxes.map((checkbox, index) => {
          const optionId = `${id}-option-${index}`;
          const messageId = `${optionId}-option-${index}`;
          return (
            <CheckboxPanel className="v-align-items-start" key={optionId} htmlFor={optionId}>
              <Utility vFlex vGap={2} style={{ inlineSize: '100%' }}>
                <Checkbox aria-describedby={messageId} className="v-flex-shrink-0" id={optionId} name={optionId} />
                <Utility vFlex vFlexCol vGap={2} vMarginVertical={8}>
                  {checkbox.label}
                  <InputMessage id={messageId}>{checkbox.message}</InputMessage>
                </Utility>
              </Utility>
            </CheckboxPanel>
          );
        })}
      </Utility>
    </fieldset>
  );
};

```

### Checkbox panel group with error
- **Section**: Checkbox panels group
- **URL**: components/checkbox/error-group-panel-checkbox
- **Tags**: docs
```tsx
import { VisaErrorTiny } from '@visa/nova-icons-react';
import { FormEvent, useRef, useState } from 'react';
import { Button, Checkbox, CheckboxPanel, InputMessage, Typography, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'error-group-panel-checkbox';

type Option = {
  checked: boolean;
  label: string;
  value: string;
  message?: string;
};

const defaultOptions: Option[] = [
  {
    checked: false,
    label: 'Label 1',
    message: 'This is optional text that describes the label in more detail.',
    value: 'label-1',
  },
  {
    checked: false,
    label: 'Label 2',
    message: 'This is optional text that describes the label in more detail.',
    value: 'label-2',
  },
  {
    checked: false,
    label: 'Label 3',
    message: 'This is optional text that describes the label in more detail.',
    value: 'label-3',
  },
];

export const ErrorPanelGroupCheckbox = () => {
  const checkboxRefs = useRef<(HTMLInputElement | null)[]>([]);
  const [options, setOptions] = useState(defaultOptions);
  const [invalid, setInvalid] = useState(false);

  const onCheckboxChange = (event: FormEvent<HTMLInputElement>, index: number) => {
    const { checked } = event.currentTarget;
    const newOptions = [...options];
    newOptions[index].checked = checked;
    setOptions(newOptions);
  };

  const onSubmit = () => {
    // Check if any of the checkbox are checked
    const isInvalid = !options.some(checkbox => checkbox.checked);
    // Set invalid state
    setInvalid(isInvalid);
    // If invalid focus on the first checkbox
    if (isInvalid) checkboxRefs.current[0]?.focus();
  };

  return (
    <>
      <fieldset aria-labelledby={`${id}-legend`}>
        <Typography aria-describedby={`${id}-message`} id={`${id}-legend`} tag="legend" variant="label">
          Group Label
        </Typography>
        <Utility vFlex vFlexCol vGap={8}>
          {options.map((option, index) => {
            const optionId = `${id}-option-${index}`;
            const messageId = `${optionId}-message`;
            return (
              <Utility element={<CheckboxPanel />} htmlFor={optionId} key={optionId} vAlignItems="start">
                <Utility vFlex vGap={2} style={{ inlineSize: '100%' }}>
                  <Checkbox
                    aria-describedby={messageId}
                    aria-invalid={invalid}
                    checked={option.checked}
                    className="v-flex-shrink-0"
                    id={optionId}
                    onChange={event => onCheckboxChange(event, index)}
                    ref={ref => {
                      checkboxRefs.current[index] = ref;
                    }}
                    value={option.value}
                  />
                  <Utility vFlex vFlexCol vGap={2} vMarginVertical={8}>
                    {option.label}
                    <InputMessage id={messageId}>{option.message}</InputMessage>
                  </Utility>
                </Utility>
              </Utility>
            );
          })}
        </Utility>
        <InputMessage aria-atomic="true" aria-live="assertive" id={`${id}-message`} role="alert" variant="body-3">
          {invalid && (
            <>
              <VisaErrorTiny />
              This is required text that describes the error in more detail.
            </>
          )}
        </InputMessage>
      </fieldset>
      <Button onClick={onSubmit}>Submit</Button>
    </>
  );
};

```

## Property Sections
### Checkbox
- **Selector**: <Checkbox />
- **Description**: Interactive element enabling users to select one or more independent options from a group.

### CheckboxPanel
- **Selector**: <CheckboxPanel />
- **Description**: Container to be used with checkbox component to add border and background color.

## Properties
### indeterminate
- **Section**: Checkbox
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Whether a checkbox is indeterminate state, only allowable on "input" tag types. This should only be set to true if checked is false.

### ref
- **Section**: Checkbox
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Checkbox
- **Type**: "symbol" , "object" , "a" , "abbr" , "address" , "area" , "article" , "aside" , "audio" , "b" , "base" , "bdi" , "bdo" , "big" , "blockquote" , "body" , "br" , "button" , "canvas" , ... 159 more ... , ComponentType
- **Default**: input
- **Required**: false
- **Description**: Tag of Component

### ref
- **Section**: CheckboxPanel
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: CheckboxPanel
- **Type**: ElementType
- **Default**: 
- **Required**: false
- **Description**: Tag of Component

