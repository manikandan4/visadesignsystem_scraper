# use-focus-trap

## Metadata
- **Version**: 0.0.1
- **Description**: This hook is used to trap focus inside a container.
- **Category**: hooks

## Example Sections
1. **Behavior and usage**
   - Description: 

## Examples
### 
- **Section**: Behavior and usage
- **URL**: hooks/use-focus-trap/use-focus-trap-example
- **Tags**: 
```tsx
import {
  Button,
  Dialog,
  DialogCloseButton,
  DialogContent,
  DialogHeader,
  Typography,
  useFocusTrap,
  Utility,
} from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'use-focus-trap-usage';

export const UseFocusTrapExample = () => {
  const { onKeyNavigation, ref } = useFocusTrap();

  return (
    <>
      <Button onClick={() => ref.current?.showModal()}>Open dialog</Button>
      <Dialog
        aria-describedby={`${id}-description`}
        aria-labelledby={`${id}-title`}
        id={id}
        ref={ref}
        onKeyDown={e => onKeyNavigation(e, ref.current?.open)}
      >
        <DialogContent>
          <DialogHeader id={`${id}-title`}>Default title</DialogHeader>
          <Typography id={`${id}-description`}>
            This is required text that describes the dialog title in more detail.
          </Typography>
          <Utility vAlignItems="center" vFlex vFlexWrap vGap={8} vJustifyContent="end" vPaddingTop={16}>
            <Button>Primary action</Button>
            <Button colorScheme="secondary">Secondary action</Button>
          </Utility>
        </DialogContent>
        <DialogCloseButton onClick={() => ref.current?.close()} />
      </Dialog>
    </>
  );
};

```

