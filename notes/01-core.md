# Split seconds into duration fields: implementation

## What the example does

Repeated division separates whole seconds into days, hours, minutes and seconds. This is elapsed duration, not a calendar month or year.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
90061
```

Expected result:

```json
{
  "days": 1,
  "hours": 1,
  "minutes": 1,
  "seconds": 1
}
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
