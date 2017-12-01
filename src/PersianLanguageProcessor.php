<?php
namespace MehrdadDadkhah\Language;

use Symfony\Component\Process\Exception\ProcessFailedException;
use Symfony\Component\Process\Process;

/**
 * simple php and python wrapper on hazm persian text processor.
 */
class PersianLanguageProcessor
{
    public function __call($method, $args)
    {
        $command = 'python ' . dirname(__FILE__) . '/processor.py ' . $method . ' ' . escapeshellarg(json_encode($args[0]));

        $process = new Process($command);
        $process->run();

        if (!$process->isSuccessful()) {
            throw new ProcessFailedException($process);
        }

        return json_decode($process->getOutput(), true);
    }
}
