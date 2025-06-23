# use-debounce

## Metadata
- **Version**: 0.0.1
- **Description**: Debounces expensive function, only calling the function after it's last call has waited for specified delay
- **Category**: hooks

## Example Sections
1. **Behavior and usage**
   - Description: 

## Examples
### 
- **Section**: Behavior and usage
- **URL**: hooks/use-debounce/use-button-debounce-example
- **Tags**: 
```tsx
import { Button, Typography, Utility, useDebounce } from '@visa/nova-react';
import { VisaInformationTiny, VisaSuccessTiny } from "@visa/nova-icons-react";
import { useState, CSSProperties } from 'react';

export const UseButtonDebounceExample = () => {
  const [success, setSuccess] = useState(false);

  const onDebouncedClick = useDebounce(() => {
    setSuccess(true);
  }, 1000);

  return (
    <Utility vFlex vFlexCol vGap={12}>
      <Typography tag="span" variant="body-2-bold">
        Rapidly click the button in sequence, then wait for one second:
      </Typography>

      <Utility vFlex vFlexRow vGap={12}>
        <Button onClick={onDebouncedClick}>Submit debounced</Button>
        <Button colorScheme="secondary" onClick={() => setSuccess(false)}>
          Reset
        </Button>
      </Utility>

      <Typography aria-atomic="true" aria-live="assertive" style={{lineHeight: '16px'}}>
        {success ? <VisaSuccessTiny style={{ '--v-icon-primary': 'green', '--v-icon-secondary': 'var(--v-message-text-success)', marginInlineEnd: '3px', verticalAlign: 'bottom' } as CSSProperties} /> : 
        <VisaInformationTiny style={{ '--v-icon-primary': 'var(--palette-default-text-subtle)', '--v-icon-secondary': 'var(--palette-default-text-subtle)', marginInlineEnd: '3px', verticalAlign: 'bottom' } as CSSProperties} />}
        {success ? 'Button click successful, many thanks' : 'Waiting for button click'}
      </Typography>
    </Utility>
  );
};

```

